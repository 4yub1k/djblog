from pytest_factoryboy import register
from .factories import PostFactory, CommentFactory, TagFactory


register(PostFactory)
register(CommentFactory)
register(TagFactory)