from django.urls import path,re_path
from booktest import views

urlpatterns = [
    path('index', views.index),
    path('create', views.create),
    re_path(r'delete(\d+)', views.delete),
]