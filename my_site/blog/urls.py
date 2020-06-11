from django.urls import path
from .views import (
    PostList,
    post_detail,
    CreatePostView,
    PostUpdateView,
    DeletePostView,
)

app_name = 'blog'
urlpatterns = [
    # post views
    path('', PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('create/post/', CreatePostView.as_view(), name='create_post'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', DeletePostView.as_view(), name='post_delete'),
]
