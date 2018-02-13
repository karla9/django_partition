# -*- coding: UTF-8 -*-


# =====================================================================
# database configurations
# =====================================================================
DATABASE_SHARD_SETTING = [
    {
        'tables': ['shop_customer_tab',
                   ],
        'key': 'shop_id',
        'rule': 'mod',
        'divisor': 10,
        'format': '02u',
    },
    # {
    #     'tables': [
    #                'customer_credit_history_tab',
    #                ],
    #     'key': 'customer_id',
    #     'rule': 'mod',
    #     'divisor': 100,
    #     'format': '08u',
    # },
    # {
    #     'tables': ['customer_login_history_tab',
    #                'customer_logout_history_tab'],
    #     'key': 'add_time',
    #     'rule': 'timestamp',
    #     'format': '%Y%m%d',
    #     'zfill': 8,
    # },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'example_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 600,
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8'},
        'SHARD': DATABASE_SHARD_SETTING,
    }
}
