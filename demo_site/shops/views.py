# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from shops.models import Shop


def index(request):
    shop_list = list(Shop.objects.all())
    return HttpResponse(', '.join(str(shop) for shop in shop_list))
