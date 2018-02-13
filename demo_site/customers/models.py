# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from djangoext.db import models


class ShopCustomer(models.PartitionModel):
    shop_id = models.PositiveBigIntegerField()
    name = models.VarCharField()
    mobile_number = models.VarCharField()

    class Meta:
        app_label = 'example'
        db_table = 'shop_customer_tab'

    def __unicode__(self):
        return u'<ShopCustomer>[table: %s, id: %d, name: %s, mobile: %s]' % (
            self._meta.db_table,
            self.id,
            self.name,
            self.mobile_number
        )
