import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django_admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}