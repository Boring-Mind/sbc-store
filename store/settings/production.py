from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

# List looks like this: '.domain1, .domain007, .domain.com'
# cast needs a function, not a list, so list comprehension doesn't work
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


# Application definition

# INSTALLED_APPS += [
#     'mineapp',
# ]

# MIDDLEWARE += [
#     'memcached',
#     'whitenoise',
#     'another security',
# ]


# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
