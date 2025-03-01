# example/urls.py
from django.urls import path

from examples.views import index


urlpatterns = [
    path('', index),
]