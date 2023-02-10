from django.contrib import admin
from .models import Post, Comment, PostTag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
        filters: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/
        src: https://github.com/django/django/blob/main/django/contrib/admin/options.py
    """
    list_display = ("author", "title", "sub_title", "slug", "content", "is_published", "post_on",
                    "post_edited",)
    summernote_fields = ("content",)
    list_editable = ("is_published", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass
