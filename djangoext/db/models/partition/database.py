from copy import deepcopy


def register_partition_databases(databases, db_labels):
    for db_label in db_labels:
        if db_label not in databases:
            continue

        db_conf = databases[db_label]
        if 'SHARD' not in db_conf:
            continue

        shard_conf_list = db_conf['SHARD']

        for shard_conf in shard_conf_list:
            if 'level' in shard_conf and shard_conf['level'] == 'database':
                for value in range(shard_conf['divisor']):
                    postfix = ('%' + shard_conf['format']) % (value)
                    new_db_label = db_label + '_%s' % postfix
                    new_db_conf = deepcopy(db_conf)
                    new_db_conf['NAME'] += '_%s' % postfix
                    new_db_conf.pop('SHARD')
                    databases[new_db_label] = new_db_conf
