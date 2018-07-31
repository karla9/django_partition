class PartitionRouter(object):
    """
    A router to control all database operations on partition models
    """
    @staticmethod
    def _db_for_database_partition(model):
        if model._meta.partition['level'] == 'database':
            return 'default_' + model._meta.partition['postfix']
        return None

    def db_for_read(self, model, **hints):
        return self._db_for_database_partition(model)

    def db_for_write(self, model, **hints):
        return self._db_for_database_partition(model)
