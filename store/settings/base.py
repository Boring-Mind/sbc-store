import os
import dj_database_url
import re
from decouple import config
from django.core.exceptions import ImproperlyConfigured


def get_config_type() -> str:
    """Reads type of current configuration from settings.ini,
    and returns its name"""
    cur_config = config('CURRENT_CONFIG', default='production')
    if cur_config in ('development', 'production'):
        return cur_config
    else:
        error_msg = "Set the CURRENT_CONFIG environment variable"
        raise ImproperlyConfigured(error_msg)


def db_url_is_valid(db_url: str) -> bool:
    """Checks, that db_url fit into format
    postgres://USER:PASSWORD@HOST:PORT/"""
    regexp = r'postgres:\/\/\S+?:\S+?@\S+?:(\d{4}|)\/\S+'
    match = re.search(regexp, db_url)
    if match is None:
        return False
    return True


# APP_ROOT points to sbc-store/store/store
# ROOT points to sbc-store/store
# PUBLIC points to sbc-store/store/public
PROJECT_APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(PROJECT_APP_ROOT))
PUBLIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, 'public'))


SECRET_KEY = config('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store.apps.models',
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

ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_URL = config('DB_URL')

if not db_url_is_valid(DATABASE_URL):
    error_msg = "Set the DB_URL environment variable properly"
    raise ImproperlyConfigured(error_msg)

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static', 'store'),
)
