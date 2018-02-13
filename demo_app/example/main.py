#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def main():
    # IMPORTANT: use local import here
    from example import settings
    from djangoext import init_django_db
    init_django_db(settings.DATABASES)

    from example.views import demo_simple
    demo_simple()


if __name__ == "__main__":
    main()
