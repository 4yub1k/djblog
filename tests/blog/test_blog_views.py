import pytest

from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import PostTag

pytestmark = pytest.mark.django_db


def test_pages(client):
    """
    Check all pages are accessable.
    """
    names = [
        "index",
        "about",
        "login",
        "logout",
        "register",
    ]

    for name in names:
        response = client.get(reverse("index"))
        assert response.status_code == 200

    response = client.get(reverse("new_post"), {})
    assert response.status_code == 302  # Redirect LoginMixin

    response = client.get(reverse("edit_post", kwargs={"post_slug": "test"}))
    assert response.status_code == 302

    # for name in names:
    #     response = client.get(reverse("index"))     # change later
    #     assert response.status_code == 200


def test_login(client):
    """
    Test login is working.
    """
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200

    data = {"username": "ayubi", "password": "test123"}
    response = client.post(url, data)
    assert response.status_code == 200

    User.objects.create_user("ayubi", "test@email.com", "test123")  # Create User
    response = client.post(url, data, follow=True)  # Redirect after login
    # print(response.redirect_chain)
    assert response.redirect_chain[0][1] == 302

    response = client.post(reverse("logout"), follow=True)
    assert response.redirect_chain[0][1] == 302

    # Test logout with different redirect url.
    data["next"] = reverse("about")
    response = client.post(url, data, follow=True)
    assert b"About Me" in response.content


def test_registration(client):
    """
    Test the registration page
    """
    response = client.get(reverse("register"))  # follow --> if any redirect
    assert response.status_code == 200

    data = {
        "username": "Salahayubi",
        "email": "salaha@salah.com",
        "password1": "test123test",
        "password2": "test123test",
    }

    response = client.post(
        reverse("register"), data, follow=True
    )  # follow --> if any redirect
    assert response.redirect_chain[0][1] == 302  # [('/accounts/login/', 302)]
    assert b"login" in response.content

    """Email Validation"""
    data["email"] = "salah.com"

    response = client.post(
        reverse("register"), data, follow=True
    )  # follow --> if any redirect
    assert len(response.redirect_chain) == 0
    assert b"Register" in response.content


def test_authenticated_pages(client, post_factory, tag_factory):
    """
    Test, whether Non-Registered Users can access pages where authentication is required.
    """
    post = post_factory()
    data = {
        "author": post.author,
        "title": post.title,
        "sub_title": post.sub_title,
        "slug": post.slug,
        "content": post.content,
        "is_published": post.is_published,
        "tag": "nature",
    }

    """Check anonymous user can't add new post, permission check."""
    response = client.post(reverse("new_post"), data, follow=True)
    assert b"login" in response.content
    # print(response.redirect_chain, response.status_code)

    """Check whether anonymous user can access detail post correctly."""
    PostTag.objects.create(post_tag=post, tag=data["tag"])
    response = client.get(
        reverse("detail_post", kwargs={"post_slug": post.slug}), follow=True
    )
    assert f"{post.title}".encode() in response.content
    # print(response.content)
    # print(response.redirect_chain, response.status_code)

    """Try to edit post as anonymous user"""
    response = client.post(
        reverse("edit_post", kwargs={"post_slug": post.slug}), data, follow=True
    )
    assert b"login" in response.content
