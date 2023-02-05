import factory

from django.contrib.auth.models import User
from blog.models import Post, Comment


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


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.SubFactory(User2Factory)
    comment = "nice!!!"


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title = "salah blog test"
    sub_title = "sub_title"
    slug = "domain.com/salah-blog-test"
    content = "This is a blog"
    is_published = "Yes"
    comment = factory.SubFactory(CommentFactory)
