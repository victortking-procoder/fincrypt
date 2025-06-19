from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('article/<int:sequence>/', views.article_detail, name='article_detail'),
    path('ad-wait/', views.ad_wait, name='ad_wait'),
]

