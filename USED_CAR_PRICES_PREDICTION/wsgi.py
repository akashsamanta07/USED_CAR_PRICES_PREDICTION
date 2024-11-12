"""
WSGI config for USED_CAR_PRICES_PREDICTION project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'USED_CAR_PRICES_PREDICTION.settings')

application = get_wsgi_application()
