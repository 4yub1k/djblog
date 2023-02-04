from django.contrib import admin
from .models import Post, Comment


# @admin.register(Post, Comment)   # admin.site.register(Post)
@admin.register(Post)   # admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
        filters: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/
        src: https://github.com/django/django/blob/main/django/contrib/admin/options.py
    """
    list_display = ("author", "title", "sub_title", "slug", "content", "is_published", "post_on",
        "post_edited","comment",)
    list_editable = ("is_published", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass