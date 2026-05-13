from django.contrib import admin
from .models import (
    UserProfile, Follow, Post, Content,
    PostLike, Comment, CommentLike,
    SavePost, SavePostItem, Storia
)


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class CommentLikeInline(admin.TabularInline):
    model = CommentLike
    extra = 1


class SavePostItemInline(admin.TabularInline):
    model = SavePostItem
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ContentInline, CommentInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentLikeInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(SavePost)
class SavePostAdmin(admin.ModelAdmin):
    inlines = [SavePostItemInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(PostLike)
admin.site.register(CommentLike)
admin.site.register(SavePostItem)
admin.site.register(Storia)