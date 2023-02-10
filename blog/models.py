from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
# import uuid


class Post(models.Model):
    choices = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    content = models.TextField(max_length=2000)
    is_published = models.CharField(max_length=5, choices=choices, default='No')
    post_on = models.DateTimeField(default=timezone.now, editable=False)
    post_edited = models.DateTimeField(default=timezone.now, editable=False)

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"post_slug": self.slug})

    def save(self, *args, **kwargs):
        # if self.slug is None:
        self.slug = slugify(f'{self.title}-{self.id}')      # id -> Post class id attributes auto by django.
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    post_date = models.DateTimeField(default=timezone.now, editable=False)
    comment = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.comment


class PostTag(models.Model):
    post_tag = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="tag_post")
    tag = models.CharField(max_length=10, blank=False, unique=False)

    class Meta:
        ordering = ["tag"]

    def __str__(self) -> str:
        return self.tag
