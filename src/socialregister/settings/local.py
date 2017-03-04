# -*- coding: utf-8 -*-
"""
Django development settings for socialregister project.
"""
from . import *  # noqa


# Debug
DEBUG = True


# Application definition
INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'socialregister',
        'USER': 'vagrant'
    }
}


# Debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
