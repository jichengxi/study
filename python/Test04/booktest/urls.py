from django.contrib import admin
from django.urls import path
from booktest import views

urlpatterns = [
    path('index', views.index),
]
