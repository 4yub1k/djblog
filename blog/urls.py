from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views


urlpatterns = [
    path("", views.ListPost.as_view(), name="index"),
    path("about/", views.aboutMe, name="about"),
    path("new_post/", views.AddPost.as_view(), name="new_post"),
    path("edit_post/<slug:post_slug>/", views.UpdatePost.as_view(), name="edit_post"),
    path("delete_post/<slug:post_slug>/", views.DeletePost.as_view(), name="delete_post"),
    path("list_post/", views.TagListPost.as_view(), name="tag_list_post"),
    path("comment/", views.addComment, name="comment"),
    path("<slug:post_slug>/", views.DetailPost.as_view(), name="detail_post"),

    path("accounts/login/", LoginView.as_view(template_name="blog/account/login.html"), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/register/", views.RegisterUser.as_view(), name="register")

]
