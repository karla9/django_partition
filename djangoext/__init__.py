# -*- coding: UTF-8 -*-


def init_django_db(databases, debug=False):
    if databases is None:
        raise TypeError('can not find databases for Django initialization')

    import django
    from django.conf import settings
    django_config = {
        'DEBUG': debug,
        'DATABASES': databases,
    }
    settings.configure(**django_config)

    if hasattr(django, 'setup'):
        django.setup()

    # let django support Model.objects.filter(x__ne=3)
    from django.db.models import Field
    from djangoext.db.models.lookups import NotEqual
    Field.register_lookup(NotEqual)

