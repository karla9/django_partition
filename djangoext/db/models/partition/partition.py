# -*- coding: UTF-8 -*-


def _partition_model_new(cls, *args, **kwargs):
    return cls(*args, **kwargs)


class PartitionUtil(object):
    @staticmethod
    def get_shard_key(partition_model):
        """
        :param partition_model: like models.ShopCustomer
        :return: None or string of sharded column, like "shop_id"
        """
        shard_conf = PartitionUtil.get_shard_conf(partition_model)
        if not shard_conf:
            return None
        return shard_conf.get('key', None)

    @staticmethod
    def get_shard_conf(partition_model):
        """
        :return: example
                {
                    "table": "shop_customer_tab",
                    "key": "shop_id",
                    "rule": "mod",
                    "divisor": 10,
                    "format": "02u"
                }
        """
        # for both django models and our own partitioned tables (shop_customer_tab, etc)
        # our own partitioned tables now have _meta attribute
        # pylint: disable=protected-access
        meta_obj = partition_model._meta

        # here we don't need to consider whether user wants to use master or slave,
        # as we assume master and slave have same table structures and thus same sharding settings
        db_label = 'default'
        # try:
        #     db_label = meta_obj.in_db
        # except:
        #     db_label = 'default'
        from django.conf import settings
        if db_label not in settings.DATABASES:
            return None

        db_conf = settings.DATABASES[db_label]
        if 'SHARD' not in db_conf:
            return None

        db_table = meta_obj.db_table
        shard_conf_list = db_conf['SHARD']
        for shard_conf in shard_conf_list:
            shard_table_name_list = shard_conf['tables']
            for shard_table_name in shard_table_name_list:
                if shard_table_name.strip().lower() == db_table.strip().lower():
                    # found match, fetch the sharding settings
                    return shard_conf
        return None

    @staticmethod
    def get_sharded_postfix(shard_conf, partition_val):
        if not shard_conf:
            raise ValueError('_get_sharded_table_name(), shard_conf cannot be null')
        rule = shard_conf['rule']

        if rule.lower() == 'div':
            divisor = shard_conf['divisor']
            sharded_value = partition_val / divisor
            shard_format = shard_conf['format']
            sharded_postfix = ('%' + shard_format) % (sharded_value)
        elif rule.lower() == 'mod':
            divisor = shard_conf['divisor']
            sharded_value = partition_val % divisor
            shard_format = shard_conf['format']
            sharded_postfix = ('%' + shard_format) % (sharded_value)
        elif rule.lower() == 'crc':
            divisor = shard_conf['divisor']
            import binascii
            sharded_value = binascii.crc32(partition_val) % divisor
            shard_format = shard_conf['format']
            sharded_postfix = ('%' + shard_format) % (sharded_value)
        elif rule.lower() == 'timestamp':
            shard_format = shard_conf['format']
            from datetime import datetime
            sharded_value = datetime.fromtimestamp(int(partition_val)).strftime(shard_format)
            zfill_val = shard_conf['zfill']
            sharded_postfix = sharded_value.zfill(zfill_val)
        else:
            raise TypeError('can not get sharded value for _get_sharded_postfix()')

        # ensure it's str, not unicode
        return sharded_postfix.encode('utf8')


class PartitionModelFactory(object):
    _partition_models = {}

    @staticmethod
    def new_partitioned_model(partition_model, **kwargs):
        """
        Note: *args are omitted here as we only need the sharding key inside kwargs
        :param partition_model:
        :param kwargs: the sharding key must be provided in this, like shop_id for most of PartitionModel
        :return:
        """
        # type: (PartitionModel, dict) -> django.db.Model
        from django.db import models

        # get the value used for sharding
        partition_id = None
        shard_conf = PartitionUtil.get_shard_conf(partition_model)

        if shard_conf:
            shard_col = shard_conf['key']
            if shard_col in kwargs:
                partition_id = kwargs.get(shard_col)
            else:
                raise ValueError('column [%s] must be provided for sharded table' % shard_col)

        model_name = partition_model.__name__
        sharded_table_postfix = ''
        if partition_id is not None:
            sharded_table_postfix = PartitionUtil.get_sharded_postfix(shard_conf, partition_id)
            model_name += '_%s' % sharded_table_postfix

        model_class = PartitionModelFactory._partition_models.get(model_name)
        if model_class is not None:
            return model_class

        attrs = {}
        cls_attr_dict = dict(partition_model.__dict__)
        for key in cls_attr_dict:
            cls_attr_val = cls_attr_dict[key]
            if isinstance(cls_attr_val, models.Field):
                attrs[key] = cls_attr_val.clone()
            else:
                attrs[key] = cls_attr_val

        # base class
        for base_cls in partition_model.__bases__:
            if base_cls is PartitionModel:
                continue
            base_attr_dict = dict(base_cls.__dict__)
            for key in base_attr_dict:
                if key.startswith("__"):
                    continue

                base_attr_val = base_attr_dict[key]
                if isinstance(base_attr_val, models.Field):
                    attrs[key] = base_attr_val.clone()
                else:
                    attrs[key] = base_attr_val

        # if 'objects' in attrs:
        #     attrs['objects'] = attrs['objects'].__class__()

        from . import utils
        meta = utils.dict_to_object(partition_model.Meta.__dict__)
        if partition_id is not None:
            meta.db_table += '_%s' % sharded_table_postfix
            # TODO: should find the app_label from the models.py definition
            # meta.app_label = BaseModel.Meta.app_label
            # TODO: should also add meta.unique_together here
        attrs['Meta'] = meta
        attrs['new'] = classmethod(_partition_model_new)

        # Put local fields in the attributes
        for field in attrs["_meta"].get_fields():
            attrs[field.name] = field
        # Pop _meta since django ModelBase does not expect an Options object in the attribute
        # Note that Meta attribute still exist
        attrs.pop("_meta", None)

        model_class = type(
            model_name,
            tuple([models.Model]),
            attrs
        )

        PartitionModelFactory._partition_models[model_name] = model_class
        return model_class


class PartitionQuerySet(object):
    def __init__(self, partition_model, db_label=None):
        self.partition_model = partition_model
        self.db_label = db_label

    def create(self, **kwargs):
        model_cls = PartitionModelFactory.new_partitioned_model(self.partition_model, **kwargs)
        if model_cls is None:
            raise TypeError('can not get sharded class for cls [%r]' % self.partition_model)
        return model_cls.objects.create(**kwargs)

    def filter(self, *args, **kwargs):
        model_cls = PartitionModelFactory.new_partitioned_model(self.partition_model, **kwargs)
        if model_cls is None:
            raise TypeError('can not get sharded class for cls [%r]' % self)
        if self.db_label:
            return model_cls.objects.using(self.db_label).filter(*args, **kwargs)
        else:
            return model_cls.objects.filter(*args, **kwargs)


class PartitionManager(object):
    def __init__(self, model_cls):
        self.model_cls = model_cls

    def using(self, db_label):
        return PartitionQuerySet(db_label=db_label, partition_model=self.model_cls)

    def filter(self, *args, **kwargs):
        return PartitionQuerySet(partition_model=self.model_cls).filter(*args, **kwargs)

    def create(self, **kwargs):
        return PartitionQuerySet(partition_model=self.model_cls).create(**kwargs)


from django.db.models.base import ModelBase
class MetaClassPartitionModel(ModelBase):
    # noinspection PyInitNewSignature
    def __new__(cls, name, bases, attrs):
        if name != 'PartitionModel':
            attr_meta = attrs.get("Meta", None)
        new_class = super(MetaClassPartitionModel, cls).__new__(cls, name, bases, attrs)
        if name != 'PartitionModel':
            if attr_meta is not None:
                setattr(new_class, 'Meta', attr_meta)
            manager = attrs.get('objects', None)
            if not manager:
                new_class.objects = PartitionManager(new_class)
        return new_class


class PartitionModel(object):
    __metaclass__ = MetaClassPartitionModel

    # objects = PartitionManager()  # dynamically created in meta class

    def __new__(cls, *args, **kwargs):
        """
        case 1: that user calls:
            cart_list = []
            for i in xrange(10):
                cart = Cart(shop_id=1,name='table 1',customer_count=3,enabled=1)
                cart_list.append(cart)
            db_manager.bulk_create(cart_list)
        case 2: in cart_table.py, we writes:
            self.make_inst() which will in turn call Cart.__new__()
        :param args:
        :param kwargs:
        :return:
        """
        model_cls = PartitionModelFactory.new_partitioned_model(cls, **kwargs)
        return model_cls(*args, **kwargs)

    def save(self):
        raise RuntimeError('This method should NEVER be called')

    @classmethod
    def get_shard_conf(cls):
        shard_conf = PartitionUtil.get_shard_conf(cls)

        if shard_conf:
            shard_key = shard_conf['key']
            shard_divisor = shard_conf['divisor']
        else:
            shard_key = shard_divisor = None

        return shard_key, shard_divisor

    @classmethod
    def get_actual_model(cls, shard):
        actual_model = None

        shard_key, shard_divisor = cls.get_shard_conf()
        if shard_key and shard_divisor:
            shard = shard % shard_divisor
            actual_model = type(cls(**{shard_key: shard}))

        return actual_model
