# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from djangoext.db import models


class ShopOrder(models.PartitionModel):
    shop_id = models.PositiveBigIntegerField()
    name = models.VarCharField()
    description = models.VarCharField()

    class Meta:
        app_label = 'example'
        db_table = 'shop_order_tab'

    def __unicode__(self):
        return u'<ShopOrder>[id: %d, name: %s, description: %s]' % (
            self.id,
            self.name,
            self.description
        )
