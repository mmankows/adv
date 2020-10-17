import environ

env = environ.Env()


SECRET_KEY = env.str('DJ_SECRET_KEY')

DEBUG = env.bool('DJ_DEBUG', default=False)

INSTALLED_APPS = [
    # Django goodies
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 3rd party
    'rest_framework',
    # project
    'adv',
    'adv_datasets',
]

# TODO: Add authentication and common security stuff
#  - middlewares (CORS, XRSF etc)
#  - related settings
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'adv.urls'

DATABASES = {
    'default': env.db_url('DJ_DATABASE_DEFAULT_URL'),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    # TODO: Implement authentication
    # 'DEFAULT_AUTHENTICATION_CLASSES': None,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

SWAPI_BASE_URL = env.str('SWAPI_BASE_URL')

DATASETS_DIR = '/datasets'
