from django_filters.rest_framework import FilterSet
from .models import Comment, Storia


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'user': ['exact'],
            'post': ['exact'],
            'created_date': ['lt', 'gt'],
        }


class StoriaFilter(FilterSet):
    class Meta:
        model = Storia
        fields = {
            'user': ['exact'],
            'created_date': ['lt', 'gt'],
        }