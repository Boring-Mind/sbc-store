"""
ASGI config for store project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
# from decouple import config

from django.core.asgi import get_asgi_application

# DJANGO_SETTINGS_MODULE = config('SETTINGS_PATH')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings.development')

application = get_asgi_application()
