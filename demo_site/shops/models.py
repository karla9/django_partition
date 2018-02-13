# -*- coding: UTF-8 -*-
from djangoext.db import models


class Shop(models.Model):
    name = models.VarCharField()
    address = models.VarCharField()

    class Meta:
        app_label = 'example'
        db_table = 'shop_tab'

    def __unicode__(self):
        return u'<Shop>[id: %d, name: %s, addr: %s]' % (
            self.id,
            self.name,
            self.address
        )

