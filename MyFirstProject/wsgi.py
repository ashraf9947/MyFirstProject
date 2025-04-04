# wsgi.py - This file is used to deploy the Django project using WSGI servers.
# It serves as the entry point for web servers like Gunicorn or uWSGI.


"""
WSGI config for MyFirstProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstProject.settings')

application = get_wsgi_application()
