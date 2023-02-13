import pytest

pytestmark = pytest.mark.django_db

"""Post Model Testing"""


def test_post_title(post_factory):
    """
    Test the post title.
    """
    # you can pass args from here too, post_factory(title = "salah blog test"sub_title = "sub_title")
    post = post_factory()
    assert post.title == "salah blog test"
    assert post.__str__() == "salah blog test"
    assert post.sub_title == "sub_title"


def test_post_author(post_factory):
    """
    Test the post author.
    """
    post = post_factory()
    assert post.author.username == "Salah"


def test_post_slug(post_factory):
    """
    Test the post slug.
    """
    post = post_factory()
    assert post.slug == "salah-blog-test-2"


"""Comment Model Testing"""


def test_comment_author(comment_factory):
    """
    Test the comment author.
    """
    comment = comment_factory()
    assert comment.author.username == "Ayubi"
    assert comment.__str__() == "Nice Post"


def test_comment_post_title(comment_factory):
    """
    Test the relation between Comment and Post models, on which post comment is posted.
    """
    comment = comment_factory()
    assert comment.post_name.title == "salah blog test"


def test_comment(comment_factory):
    """
    Test the comment.
    """
    comment = comment_factory()
    assert comment.comment == "Nice Post"


"""Tag Model Testing"""


def test_tag_post(tag_factory):
    """
    Test to which post the tag belongs.
    """
    tag = tag_factory()
    assert tag.post_tag.title == "salah blog test"


def test_tag(tag_factory):
    """
    Test the tag.
    """
    tag = tag_factory()
    assert tag.tag == "nature"
