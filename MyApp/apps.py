# apps.py - Configuration settings for this Django application.

from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyApp'
