from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    post_date = models.DateTimeField(default=timezone.now, editable=False)
    comment = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.comment


class Post(models.Model):
    choices = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField(max_length=800)
    is_published = models.CharField(max_length=5, choices=choices, default='No')
    post_on = models.DateTimeField(default=timezone.now, editable=False)
    post_edited = models.DateTimeField(default=timezone.now, editable=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
