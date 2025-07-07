"""
WSGI config for easyads project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Skip migration checks in maintenance mode
if os.getenv("SKIP_DJANGO_MIGRATION_CHECK"):
    from django.apps.registry import apps
    if not apps.ready:
        apps.skip_check(apps.EVERY_CHECK)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyads.settings')

application = get_wsgi_application()
