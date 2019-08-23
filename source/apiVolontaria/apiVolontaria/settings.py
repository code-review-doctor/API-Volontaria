"""
Django settings for apiVolontaria project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_u0yee1g84_g9l89ip@vkw2(03c8ax6esl-6%d471oe5%17-_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_docs',
    'rest_framework.authtoken',
    'corsheaders',
    'import_export',
    'anymail',
    'orderable',
    'ckeditor',
    'reversion',

    'apiVolontaria',
    'volunteer',
    'location',
    'coupons',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'apiVolontaria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/apiVolontaria/templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apiVolontaria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.'
                'auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.'
                'auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.'
                'auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.'
                'password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Local path
LOCALE_PATHS = (
    'apiVolontaria/locale',
    'location/locale',
    'order/locale',
    'volunteer/locale',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

# Django Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apiVolontaria.authentication.TemporaryTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.'
                                'LimitOffsetPagination',
    'PAGE_SIZE': 100
}


# CORS Header Django Rest Framework

CORS_ORIGIN_ALLOW_ALL = True


# Temporary Token

REST_FRAMEWORK_TEMPORARY_TOKENS = {
    'MINUTES': 10,
    'RENEW_ON_SUCCESS': True,
    'USE_AUTHENTICATION_BACKENDS': False,
}

# Activation Token

ACTIVATION_TOKENS = {
    'MINUTES': 2880,
}

# Email service configuration (using Anymail).
# Refer to Anymail's documentation for configuration details.

ANYMAIL = {
    "SENDINBLUE_API_KEY": "SENDINBLUE_API_KEY",
    'TEMPLATES': {
        "CONFIRM_SIGN_UP": "example_template_id",
        "FORGOT_PASSWORD": "example_template_id",
        "COUPON": "example_template_id",
    },
}
EMAIL_BACKEND = 'anymail.backends.sendinblue.EmailBackend'
# This 'FROM' email is not used with SendInBlue templates
DEFAULT_FROM_EMAIL = 'noreply@example.org'

COUPON_SEND_EMAIL = False

# These settings are not related to the core API functionality. Feel free to
# edit them to your needs.
# NOTE: "{{token}}" is a placeholder for the real activation token. It will be
#       dynamically replaced by the real "token".
CONSTANT = {
    "ORGANIZATION": "NousRire",
    "EMAIL_SERVICE": False,
    "AUTO_ACTIVATE_USER": False,
    "FRONTEND_INTEGRATION": {
        "ACTIVATION_URL": "example.com/activate?activation_token={{token}}",
        "FORGOT_PASSWORD_URL": "example.com/forgot_password?token={{token}}",
    },
}


try:
    from apiVolontaria.local_settings import *
except ImportError:
    pass
