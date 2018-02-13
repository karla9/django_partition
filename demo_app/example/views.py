# -*- coding: UTF-8 -*-
from example import models


def demo_simple():
    shop_info = models.Shop(
        name='My Shop',
        address='My Address'
    )
    shop_info.save()


def demo_partition():
    from random import randint
    shop_id = randint(1, 10)
    shop_customer = models.ShopCustomer(
        shop_id=shop_id,
        name='Customer 1',
        mobile_number='123456'
    )
    shop_customer.save()
    print('shop_id=%s' % shop_id)
