"""drfdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path

from apps import views
from rest_framework import routers

# 实例化类 得到两个对象
# routers.DefaultRouter() #有根路由，路由更多更多
# routers.SimpleRouter()
router = routers.SimpleRouter()
# 注册
router.register('books7', views.BookView7, basename='books7')
print(router.urls)
'''
[
<URLPattern '^books7/$' [name='book-list']>, 
<URLPattern '^books7\.(?P<format>[a-z0-9]+)/?$' [name='book-list']>, 
<URLPattern '^books7/(?P<pk>[^/.]+)/$' [name='book-detail']>, 
<URLPattern '^books7/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='book-detail']>, 
<URLPattern '^$' [name='api-root']>, 
<URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
]
'''


urlpatterns = [
    #    path('admin/', admin.site.urls),
    re_path('books/(?P<pk>\d+)', views.BookView.as_view()),
    path('books/', views.BooksView.as_view()),
    path('booksmodel/', views.BooksModelView.as_view()),

    path('books2/', views.BooksView2.as_view()),
    re_path('books2/(?P<pk>\d+)', views.BookView2.as_view()),

    path('books3/', views.BooksView3.as_view()),
    re_path('books3/(?P<pk>\d+)', views.BookView3.as_view()),

    path('books4/', views.BooksView4.as_view()),
    re_path('books4/(?P<pk>\d+)', views.BookView4.as_view()),

    path('books5/', views.BookView5.as_view(actions={'get': 'list', 'post': 'create'})),
    re_path('books5/(?P<pk>\d+)', views.BookView5.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('books6/', views.BookView6.as_view(actions={'get': 'list'})),
    re_path('books6/(?P<pk>\d+)', views.BookView6.as_view(actions={'get': 'retrieve'})),

    path('login/', views.LoginView.as_view()),
]

# 加到urlpatterns里
urlpatterns += router.urls

