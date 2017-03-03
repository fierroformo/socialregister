# -*- coding: utf-8 -*-
"""
Django settings for socialregister project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*p_&!3^v6@n_&wy7l_ewpe3e-6cxg@qa-38hw9uu=k=w7f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (
    ('Alejandro Betancourt', 'fierroformo@gmail.com'),
)

ALLOWED_HOSTS = ['socialregister.local']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'socialregister.users',
    'crispy_forms',
    'social_django',
    'markdown_deux',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ROOT_URLCONF = 'socialregister.urls'

WSGI_APPLICATION = 'socialregister.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/assets/'

STATICFILES_DIRS = (
    os.path.realpath(os.path.join(BASE_DIR, '..', 'assets')),
)

STATIC_ROOT = os.path.realpath(
    os.path.join(BASE_DIR, '..', '..', 'media', 'assets')
)


# Template settings
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.realpath(os.path.join(BASE_DIR, '..', 'templates'))
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'social_django.context_processors.backends',
            'social_django.context_processors.login_redirect',
        ],
        'debug': DEBUG
    }
}]

AUTH_USER_MODEL = 'users.User'

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.realpath(os.path.join(
    BASE_DIR, '..', '..', 'media', 'email'
))

# Social settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.live.LiveOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
)

SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_ALWAYS_ASSOCIATE = True

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'socialregister.users.pipeline.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_LOGIN_URL = 'users:login'
