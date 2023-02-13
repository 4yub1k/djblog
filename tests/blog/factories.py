import factory

from django.contrib.auth.models import User
from blog.models import Post, Comment, PostTag
from django.utils.text import slugify


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "Salah"
    password = "12345"
    email = "test@test.com"
    is_superuser = False
    is_active = True


class User2Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "Ayubi"
    password = "12345"
    email = "test1@test.com"
    is_superuser = False
    is_active = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = 2
    author = factory.SubFactory(UserFactory)
    title = "salah blog test"
    sub_title = "sub_title"
    slug = slugify(f'{title}-{id}')
    content = "This is a blog",
    is_published = "Yes",


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.SubFactory(User2Factory)
    post_name = factory.SubFactory(PostFactory)
    comment = "Nice Post"


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostTag

    post_tag = factory.SubFactory(PostFactory)
    tag = "nature"
