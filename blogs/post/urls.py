
from django.urls import path
from .views import PostListView, PostDetailView, add_comment_to_post

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
]