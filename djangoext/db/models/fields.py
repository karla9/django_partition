# -*- coding: UTF-8 -*-
from django.db.models import fields


class VarCharField(fields.CharField):
    # A basically CharField with max_length optional
    description = "optional max_length string"

    def __init__(self, max_length=4000, *args, **kwargs):
        kwargs['max_length'] = max_length  # Satisfy management validation.
        super(VarCharField, self).__init__(*args, **kwargs)
        # Don't add max-length validator like CharField does.

    def get_internal_type(self):
        # This has no function, since this value is used as a lookup in
        # db_type().  Put something that isn't known by django so it
        # raises an error if it is ever used.
        return 'VarCharField'

    def db_type(self, connection):
        # *** This is probably only compatible with Postgres.
        # 'varchar' with no max length is equivalent to 'text' in Postgres,
        # but put 'varchar' so we can tell LongCharFields from TextFields
        # when we're looking at the db.
        return 'varchar'


class TinyIntegerField(fields.SmallIntegerField):
    def db_type(self, connection):
        return "TINYINT"

    def formfield(self, **kwargs):
        defaults = {'min_value': -128, 'max_value': 127}
        defaults.update(kwargs)
        return super(TinyIntegerField, self).formfield(**defaults)


class PositiveTinyIntegerField(fields.PositiveSmallIntegerField):
    def db_type(self, connection):
        return "TINYINT UNSIGNED"

    def formfield(self, **kwargs):
        defaults = {'min_value': 0, 'max_value': 255}
        defaults.update(kwargs)
        return super(PositiveTinyIntegerField, self).formfield(**defaults)


class PositiveAutoField(fields.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.__class__.__module__:
            return 'UNSIGNED AUTO_INCREMENT'
        return super(PositiveAutoField, self).db_type(connection)

    def formfield(self, **kwargs):
        defaults = {'min_value': 0, 'max_value': 2 ** 32 - 1}
        defaults.update(kwargs)
        return super(PositiveAutoField, self).formfield(**defaults)


class PositiveBigIntegerField(fields.BigIntegerField):
    empty_strings_allowed = False

    def db_type(self, connection):
        return "BIGINT UNSIGNED"

    def formfield(self, **kwargs):
        defaults = {'min_value': 0, 'max_value': fields.BigIntegerField.MAX_BIGINT * 2 + 1}
        defaults.update(kwargs)
        return super(PositiveBigIntegerField, self).formfield(**defaults)


class BigAutoField(fields.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.__class__.__module__:
            return 'BIGINT AUTO_INCREMENT'
        return super(BigAutoField, self).db_type(connection)

    def formfield(self, **kwargs):
        defaults = {'min_value': -fields.BigIntegerField.MAX_BIGINT - 1, 'max_value': fields.BigIntegerField.MAX_BIGINT}
        defaults.update(kwargs)
        return super(BigAutoField, self).formfield(**defaults)


class PositiveBigAutoField(fields.AutoField):
    def db_type(self, connection):
        if 'mysql' in connection.__class__.__module__:
            return 'BIGINT UNSIGNED AUTO_INCREMENT'
        return super(PositiveBigAutoField, self).db_type(connection)

    def formfield(self, **kwargs):
        defaults = {'min_value': 0, 'max_value': fields.BigIntegerField.MAX_BIGINT * 2 + 1}
        defaults.update(kwargs)
        return super(PositiveBigAutoField, self).formfield(**defaults)
