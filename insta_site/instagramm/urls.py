from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('follow/', FollowListAPIView.as_view(), name='follow_list'),
    path('follow/create/', FollowCreateAPIView.as_view(), name='follow_create'),
    path('follow/<int:pk>/delete/', FollowDeleteAPIView.as_view(), name='follow_delete'),
    path('posts/', PostListAPIView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post_update'),
    path('contents/create/', ContentCreateAPIView.as_view(), name='content_create'),
    path('post-likes/', PostLikeListAPIView.as_view(), name='post_like_list'),
    path('post-likes/create/', PostLikeCreateAPIView.as_view(), name='post_like_create'),
    path('comments/', CommentListAPIView.as_view(), name='comment_list'),
    path('comments/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/', CommentUpdateAPIView.as_view(), name='comment_update'),
    path('comment-likes/create/', CommentLikeCreateAPIView.as_view(), name='comment_like_create'),
    path('save-post/<int:pk>/', SavePostDetailAPIView.as_view(), name='save_post_detail'),
    path('save-post/items/create/', SavePostItemCreateAPIView.as_view(), name='save_post_item_create'),
    path('save-post/items/<int:pk>/delete/', SavePostItemDeleteAPIView.as_view(), name='save_post_item_delete'),
    path('storias/', StoriaListAPIView.as_view(), name='storia_list'),
    path('storias/create/', StoriaCreateAPIView.as_view(), name='storia_create'),
    path('storias/<int:pk>/delete/', StoriaDeleteAPIView.as_view(), name='storia_delete'),
]