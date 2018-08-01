#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoext_site.settings")
    try:
        from django.core.management import execute_from_command_line

        from djangoext.db.models import register_partition_databases
        register_partition_databases(['default', ])

        # Add partition to Options default names.
        from django.db.models import options
        extra_default_names = ('partition',)
        options.DEFAULT_NAMES = options.DEFAULT_NAMES + extra_default_names
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    execute_from_command_line(sys.argv)
