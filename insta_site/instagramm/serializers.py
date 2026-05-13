from rest_framework import serializers
from .models import (
    UserProfile, Follow, Post, Content,
    PostLike, Comment, CommentLike,
    SavePost, SavePostItem, Storia
)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'username']


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'username', 'date_registered']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'file']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['id', 'user', 'like', 'dislike']


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    likes = CommentLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_date', 'likes']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user', 'like']


class PostListSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'music', 'contents']


class PostDetailSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = PostLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'music', 'contents', 'comments', 'likes']


class SavePostItemSerializer(serializers.ModelSerializer):
    post = PostListSerializer()

    class Meta:
        model = SavePostItem
        fields = ['id', 'post']


class SavePostSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    items = SavePostItemSerializer(many=True, read_only=True)

    class Meta:
        model = SavePost
        fields = ['id', 'user', 'items']


class StoriaSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Storia
        fields = ['id', 'user', 'file', 'created_date']