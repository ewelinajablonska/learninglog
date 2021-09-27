"""Defines URL patterns for learning_log."""

from django.urls import path

from . import views

app_name = 'learning_log'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
]