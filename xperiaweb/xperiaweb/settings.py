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

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'camera.apps.CameraConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'global_login_required.GlobalLoginRequiredMiddleware',
]

PUBLIC_PATHS = [
    '/accounts/*',
]

ROOT_URLCONF = 'xperiaweb.urls'

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

WSGI_APPLICATION = 'xperiaweb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'assets'),
]
STATIC_ROOT = '/var/www/seima-kinjo.com/html/static'
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