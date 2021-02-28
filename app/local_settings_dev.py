import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'apogeu',
        'USER': 'apogeu',
        'PASSWORD': 'secret',
        'HOST': 'db',
        'PORT': 5432,
    }
}

DJANGO_PATH = "/usr/src/apogeu"
