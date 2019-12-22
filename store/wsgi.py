"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from store.settings.base import get_config_type

# set path to the current config file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings.' + get_config_type())

application = get_wsgi_application()
