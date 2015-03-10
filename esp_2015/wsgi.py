"""
WSGI config for esp_2015 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

VENV_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

sys.path.append(PROJECT_ROOT)

activate_this = os.path.join(VENV_ROOT, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esp_2015.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
