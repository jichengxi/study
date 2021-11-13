from django.contrib import admin
from django.urls import path
from booktest import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('login_check', views.login_check),
]
