# -*- coding: utf-8 -*-
from django.http import HttpResponse
from customers.models import ShopCustomer


def index(request):
    customer_list = list(ShopCustomer.objects.filter(shop_id=9))
    return HttpResponse(', '.join(str(customer) for customer in customer_list))
