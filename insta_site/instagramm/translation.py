from .models import (
    UserProfile, Post, Comment, Storia
)
from modeltranslation.translator import TranslationOptions, register


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)