"""
Django settings for firstsite project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-a!toe%q+xv1r_9(fod1lesfqk@7fn92@i&da2zrdb+)s8)-6_l'
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.2.3.4',
    '127.3.3.3',
    '127.0.0.1',
    'localhost',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'bootstrap4',
    'captcha',
    'precise_bbcode',
    'django_cleanup',
    'easy_thumbnails',
    'django_redis',
    'rest_framework',
    'corsheaders',

    'bboard.apps.BboardConfig',
    'testapp.apps.TestappConfig',
    'authapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',  # lesson_49

    'django.middleware.common.CommonMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # 'bboard.middlewares.my_middleware',
    # 'bboard.middlewares.MyMiddleware',
    # 'bboard.middlewares.RubricsMiddleware',
]

ROOT_URLCONF = 'firstsite.urls'

# ABSOLUTE_URL_OVERRIDES = {
#     # 'bboard.rubric': lambda rec: "/bboard/%s/" % rec.pk,
#     # 'bboard.rubric': lambda rec: f"/bboard/{rec.pk}/",
#     'bboard.rubric': lambda rec: f"/{rec.pk}/",
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # 'NAME': "",
        # 'DIRS': [BASE_DIR / 'templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        # 'debug': False,
        'OPTIONS': {
            # 'autoescape': True,
            # 'string_if_invalid': "Бобер перегрыз провода",
            # 'file_charset': 'utf-8',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',

                'bboard.context_pocessors.rubrics',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # 'libraries': {
            #     'filtersandtags': 'bboard.filtersandtags',
            #     'ft': 'bboard.filtersandtags',
            # },
            # 'builtins': [
            #     'bboard.filtersandtags',
            # ],
        },
    },
]

WSGI_APPLICATION = 'firstsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'ATOMIC_REQUEST': False,
        # 'AUTOCOMMIT': True,
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "firstsite",
#         # "USER": "postgres",
#         # "PASSWORD": "gg356g",
#         # "HOST": "127.0.0.1",
#         # "PORT": "5432",
#         "USER": env('USER'),
#         "PASSWORD": env('PASSWORD'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {'max_similarity': 0.7},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # 'OPTIONS': {'password_list_pass': 'какой-то путь'},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'firstsite.validators.NoForbiddenCharsValidator',
        'OPTIONS': {'forbidden_chars': (' ', ',', '.', ':', ';')},
    },
]

AUTH_USER_MODEL = 'authapp.BbUser'

DEFAULT_CHARSET = 'utf-8'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True
USE_L18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = 'index'

# Настройки каптчи
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 6
CAPTCHA_TIMEOUT = 1
CAPTCHA_LETTER_ROTATION = (-15, 15)

BBCODE_SMILIES_UPLOAD_TO = 'static/precise_bbcode/smiles'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {
    'bboard.Bb.picture': {
        'default': {
            'size': (500, 300),
            'crop': 'scale',
        },
    },
    'testapp': {
        'default': {
            'size': (400, 300),
            'crop': 'smart',
            'bw': True,
        },
    },
    '': {
        'default': {
            'size': (180, 240),
            'crop': 'scale',
        },
        'big': {
            'size': (480, 640),
            'crop': '10,10',
        },
    },
}
THUMBNAIL_DEFAULT_OPTIONS = {'quality': 90, 'subsampling': 1, }
THUMBNAIL_BASEDIR = 'thumbs'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MESSAGE_LEVEL = 20
# from django.contrib import messages
# MESSAGE_LEVEL = messages.DEBUG
MESSAGE_TAGS = {
    100: 'text-warning',  # lesson_44_hw
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_USE_LOCALE = True
EMAIL_FILE_PATH = 'tmp/messages'

ADMINS = [
    ('Admin1', 'admin1@supersite.ru'),
    ('Admin2', 'admin2@othersite.ru'),
    ('MegaAdmin', 'megaadmin@megasite.ru'),
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cache_table',
#         'TIMEOUT': 120,
#         'OPTIONS': {
#             'MAX_ENTRIES': 200,
#         }
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',  # 'LOCATION': 'localhost:11211',
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'file-cache'),
#     }
# }

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "mysecret"
        }
    }
}

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:5500',
    'https://localhost:5500',
]

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     )
# }
