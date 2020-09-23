from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('ajax-article-list/', views.ajax_article_list, name='ajax_article_list'),
    path('ajax-article-detail/', views.ajax_article_detail, name='ajax_article_detail'),
]