from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from comments.models import Comment
from posts.models import Category, Post


class CommentInline(GenericTabularInline):
    model = Comment
    '''
    ct_field = "content_type" # default value is content_type.
    ct_fk_field = "object_id" # default value is object_id.
    '''


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["id", "title", "created", "get_category"]
    inlines = [
        CommentInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
