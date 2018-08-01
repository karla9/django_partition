# -*- coding: utf-8 -*-
from django.http import HttpResponse
from orders.models import ShopOrder


def index(request):
    order_list = list(ShopOrder.objects.filter(shop_id=9))
    return HttpResponse(', '.join(str(order) for order in order_list))
