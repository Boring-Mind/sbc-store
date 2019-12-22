"""
ASGI config for store project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from store.settings.base import get_config_type

# set path to the current config file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings.' + get_config_type())

application = get_asgi_application()
