# -*- coding: UTF-8 -*-


class MyObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def dict_to_object(d):
    return MyObject(**d)


def create_object(**kwargs):
    return MyObject(**kwargs)

