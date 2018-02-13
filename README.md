# django_partition

This package aims to provide an easy-to-use way to support "table partition" in Django.

advantages:
* easy to use: same (almost) as normal Django models
* easy to port: just several simple steps, you can make your own app support partition
* easy to change later: you can make your app "non-partitioned" at first, then switch to partitioned mode

# for Django projects

how-to:
* copy **djangoext** package to root folder of your django project;
* modify the "settings.py", define your "SHARD" section in "DATABASES"
* in models.py of your Django apps:
    * use "from djangoext.db" instead of "from django.db"
    * inherit from models.PartitionModel instead of models.Model


# for non-Django apps (only use Django orm)

how-to:
* copy **djangoext** package to root folder of your django project;
* modify the "settings.py", define your "SHARD" section in "DATABASES"
* in models.py of your Django apps:
    * use "from djangoext.db" instead of "from django.db"
    * inherit from models.PartitionModel instead of models.Model
* in entry point, invoke "djangoext.init_django_db()"


# Partition methods
currently this package supports:
* mod
* divide
* crc
* date/time
* (or add your own method in code)

