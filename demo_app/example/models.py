# -*- coding: UTF-8 -*-
from djangoext.db import models


class Shop(models.Model):
    name = models.VarCharField()
    address = models.VarCharField()

    class Meta:
        app_label = 'example'
        db_table = 'shop_tab'


class ShopCustomer(models.PartitionModel):
    shop_id = models.PositiveBigIntegerField()
    name = models.VarCharField()
    mobile_number = models.VarCharField()

    class Meta:
        app_label = 'example'
        db_table = 'shop_customer_tab'
