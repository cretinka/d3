from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('add/', views.add_news, name='add_news'),
]
