from django.urls import path
from .views import *


app_name = "article"  # for reverse namespace
urlpatterns = [
    path('', api_root),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<username>/list/', UserArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/single/', ArticleDetail.as_view(), name='article-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
]

