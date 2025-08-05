# blog_api/urls.py
from django.urls import path
from .views import PostListView, PostDetailView, SubscribeView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
