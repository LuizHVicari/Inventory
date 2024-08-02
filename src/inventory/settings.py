from pathlib import Path
import os
from loguru import logger
import sys
from decouple import config


logger.remove()
logger.add(sys.stderr, level=config('CONSOLE_LOG_LEVEL', cast=str, default='WARNING'))
logger.add('log.log', level='INFO')
logger.add('warnings.log', level='WARNING')
logger.add('critical.log', level='CRITICAL')


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

ASGI_APPLICATION = "inventory.asgi.application"

SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

DEBUG = config('DJANGO_DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'allauth',
    'allauth.account',
    'compressor',
    'widget_tweaks',
    'django_extensions',
    'channels',

    # custom
    'apps.users',
    'apps.items',
    'apps.chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'inventory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          os.path.join(BASE_DIR, 'templates'),
          os.path.join(BASE_DIR, 'templates', 'allauth'),
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

WSGI_APPLICATION = 'inventory.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', cast=str, default='django.db.backends.postgresql'),
        'NAME': config('DB_NAME', cast=str, default='inventory'),
        'USER': config('DB_USER', cast=str, default='postgres'),
        'PASSWORD': config('DB_PASSWORD', cast=str, default='postgres'),
        'HOST': config('DB_HOST', cast=str, default='localhost'),
        'PORT': config('DB_PORT', cast=str, default=5432),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LANGUAGE_CODE = 'pt-Br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# auth
ACCOUNT_ADAPTER = 'inventory.adapter.NoNewUserAccountAdapter'

LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login'

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_LOGOUT_ON_GET = True

# styles
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": config('CACHE_BACKEND', cast=str, default="channels_redis.core.RedisChannelLayer"),
        "CONFIG": {
            "hosts": [(
              config('CACHE_HOST', cast=str, default='localhost'),
              config('CACHE_PORT', cast=int, default='6379'),    
            )],
        },
    },
}