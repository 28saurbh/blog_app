from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category_documentation/', views.cat_docs, name = 'cat_docs'),
    path('all_documentation', views.all_docs, name = 'all_docs'),
    path('category_documentation/cat_blog/blog/<str:slug>', views.blog, name = 'blog'),
    path('category_documentation/cat_blog', views.cat_blog, name = 'cat_blog'),
    path('search', views.search, name = 'search_result'),
]
