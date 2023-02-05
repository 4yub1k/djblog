from pytest_factoryboy import register
from .factories import PostFactory, CommentFactory


register(PostFactory)
register(CommentFactory)