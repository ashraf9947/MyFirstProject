# urls.py - Defines URL patterns for this Django application.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage route
]
