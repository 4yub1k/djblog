from django import forms
from django.core.exceptions import ValidationError
from .views import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # fields = "__all__"
        fields = ("title", "sub_title", "content", "is_published")

    # add extra field to form (field not present in model)
    def __init__(self, user=None, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["tag"] = forms.CharField(max_length=15, required=True)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User

        # fields = ("__all__")  # set all only for ADMIN dashboard
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):  # def clean_<fieldName>(self):
        self.email = self.cleaned_data["email"]
        self.email_exists = User.objects.filter(email=self.email).exists()

        try:
            validate_email(self.email)
        except Exception:
            raise ValidationError("The email is invalid.")

        if self.email_exists:
            raise ValidationError("Ops, something went wrong")  # supress this error for privacy if needed!

        return self.email
