from copy import deepcopy
from django.conf import settings


def register_partition_databases(db_labels):
    for db_label in db_labels:
        if db_label not in settings.DATABASES:
            return

        db_conf = settings.DATABASES[db_label]
        if 'SHARD' not in db_conf:
            return

        shard_conf_list = db_conf['SHARD']

        for shard_conf in shard_conf_list:
            if 'level' in shard_conf and shard_conf['level'] == 'database':
                for value in range(shard_conf['divisor']):
                    postfix = ('%' + shard_conf['format']) % (value)
                    new_db_label = db_label + '_%s' % postfix
                    new_db_conf = deepcopy(db_conf)
                    new_db_conf['NAME'] += '_%s' % postfix
                    new_db_conf.pop('SHARD')
                    settings.DATABASES[new_db_label] = new_db_conf
