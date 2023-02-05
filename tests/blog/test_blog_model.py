import pytest


@pytest.mark.django_db
class TestBlogModel:

    def test_post_title(self, post_factory):
        # you can pass args from here too, post_factory(title = "salah blog test"sub_title = "sub_title")
        self.post = post_factory()


        assert self.post.title == "salah blog test"
        assert self.post.__str__() == "salah blog test"
        assert self.post.sub_title == "sub_title"

    def test_post_author(self, post_factory):
        post = post_factory()

        assert post.author.username == "Salah"

    def test_post_comment(self, post_factory):
        post = post_factory()

        assert post.comment.comment == "nice!!!"


@pytest.mark.django_db
class TestCommentModel:

    def test_comment_author(self, comment_factory):
        comment = comment_factory()

        assert comment.author.username == "Ayubi"
        assert comment.__str__() == "nice!!!"

    def test_comment(self, comment_factory):
        comment = comment_factory()

        assert comment.comment == "nice!!!"