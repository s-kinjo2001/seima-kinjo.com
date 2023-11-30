import environ
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(Path.joinpath(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'line_bot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'line_bot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

STATIC_ROOT = '/var/www/seima-kinjo.com/html/line_bot/static'
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
             'format': ('%(levelname)s [%(asctime)s] %(name)s %(message)s'),
        },
         'verbose': {
             'format': '%(levelname)s %(asctime)s %(name)s %(process)d %(thread)d %(message)s'
         },
     },
     'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse'
         },
         'require_debug_true': {
             '()': 'django.utils.log.RequireDebugTrue'
         },
     },
     'handlers': {
         'debug-console': {
             'level': 'ERROR',
             'filters': ['require_debug_true'],  # settings.DEBUG=Falseなら全て破棄
             'class': 'logging.StreamHandler',
             'formatter': 'verbose'
         },
         'prod-console': {
             'level': 'ERROR',
             'filters': ['require_debug_false'],  # settings.DEBUG=Trueなら全て破棄
             'class': 'logging.StreamHandler',
             'formatter': 'standard'
         },
         'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log/debug.log'),
            'formatter': 'verbose',
        },
     },
     'loggers': {
         '': {  # 'root' の代わり。全てキャッチする
             'handlers': ['prod-console', 'debug-console'],
             'level': 'NOTSET',
             'propagate': False
         },
         'django': {
             'handlers': ['prod-console', 'debug-console'],
             'level': 'ERROR',  # Djangoモジュール由来のログをERROR以上のみに制限
             'propagate': False
         },
         'django.request': {
             'handlers': ['prod-console', 'debug-console'],
             'level': 'ERROR',  # Djangoモジュール由来のログをERROR以上のみに制限
             'propagate': False,
         },
         'django.db.backends': {
             'handlers': ['prod-console', 'debug-console'],
             'level': 'DEBUG',  # DBに発行するSQLログを出力（実際の出力はhandlerの方で制御する）
             'propagate': False
         },
     }
 }