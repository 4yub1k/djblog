from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Post, Comment, PostTag
from .forms import PostForm, RegisterForm
from django_summernote.widgets import SummernoteWidget
from django import forms
# from django.forms import ValidationError


class ListPost(ListView):
    """
    List all posts.
    """
    model = Post
    paginate_by = 2
    template_name = "blog/index/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(ListPost, self).get_context_data(**kwargs)
        context['tags'] = PostTag.objects.values()   # Retrun dictionary instead of object List, dictsort in template
        context['latest'] = self.object_list.order_by("-post_on")[:5]
        return context


class DetailPost(DetailView):
    """
    Get post using the slug.
    """
    model = Post
    context_object_name = "post"
    template_name = "blog/post/detail_post.html"
    slug_url_kwarg = "post_slug"    # get post using slug


class AddPost(LoginRequiredMixin, CreateView):
    """
    Add new post.
    """
    model = Post
    context_object_name = "post"
    template_name = "blog/post/new_post.html"
    form_class = PostForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()     # in order to use the model/form instance first save it
        PostTag.objects.create(post_tag=form.instance, tag=form.cleaned_data["tag"])
        return super(AddPost, self).form_valid(form)

    # When form is invalid, what to do? also helps in debugging
    def form_invalid(self, form):
        return CreateView.form_invalid(self, form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["content"] = forms.CharField(
            widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
            required=True, max_length=2000
        )
        return form


class UpdatePost(LoginRequiredMixin, UpdateView):
    """
    Update the post using slug.
    """
    model = Post
    context_object_name = "posts"
    template_name = "blog/post/edit_post.html"
    form_class = PostForm
    success_url = reverse_lazy("index")
    slug_url_kwarg = "post_slug"

    def form_valid(self, form):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            raise PermissionDenied()

        PostTag.objects.filter(post_tag=self.object.id).update(tag=form.cleaned_data["tag"])
        return super(UpdatePost, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # check permission to edit
        if self.request.user != self.object.author:
            raise PermissionDenied()

        context = super(UpdatePost, self).get_context_data(**kwargs)
        context['tags'] = PostTag.objects.get(post_tag=self.object.id)     # use get for unique row/entry
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["content"] = forms.CharField(
            widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
            required=True, max_length=2000
        )
        return form


class DeletePost(DeleteView):
    """
    Delete the post using slug.
    """
    model = Post
    context_object_name = "post"
    slug_url_kwarg = "post_slug"
    template_name = "blog/post/delete_post.html"
    success_url = reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            # print(self.request.user, self.object)
            raise PermissionDenied()
        return super().post(request, *args, **kwargs)


class TagListPost(ListView):
    """
    Get posts by tag.
    """
    paginate_by = 3
    context_object_name = "posts"
    template_name = "blog/tag/tag_list_post.html"

    def get_queryset(self):
        self.posts = PostTag.objects.filter(tag=self.request.GET.get("tag"))
        return self.posts


class SearchPost(ListView):
    """
    Search for keyword in blog posts.
    """
    model = Post
    template_name = "blog/index/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        search = super(SearchPost, self).get_queryset()
        return search.filter(content__contains=self.request.GET.get("search"))


class RegisterUser(CreateView):
    """
    New user registeration.
    """
    # form is default context obj name
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "blog/account/register.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("index")
        return super().get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     self.email = User.objects.filter(email=form.cleaned_data["email"]).exists()

    #     if self.email:
    #         ValidationError(u"Username/Email not correct !")
    #     return super(RegisterUser, self).form_valid(form)


def addComment(request):
    """
    Add comment to post.
    """
    post = get_object_or_404(Post, pk=request.POST.get("post"))
    user = get_object_or_404(User, username=request.user.username)
    comment = Comment.objects.create(
        post_name=post, author=user, comment=request.POST.get("comment")
    )
    return render(request, "blog/comment/new_comment.html", {"comment": comment})


def aboutMe(request):
    """
    About me page.
    """
    return render(request, "blog/index/about.html")
