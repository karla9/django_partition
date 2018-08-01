# -*- coding: UTF-8 -*-

from djangoext.db.models.fields import (
    VarCharField,
    TinyIntegerField, PositiveTinyIntegerField,
    PositiveBigIntegerField,
    PositiveAutoField, BigAutoField, PositiveBigAutoField
)
from djangoext.db.models.partition import (
	register_partition_databases,
	PartitionModel,
	PartitionRouter
)
from djangoext.db.models.lookups import NotEqual

from django.db.models import *  # to put everything into namespace djangoext.db.models
