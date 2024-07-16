from django.contrib.auth.forms import UserCreationForm
from .models import User, Book
from django.forms import ModelForm
from django import forms

# from django.core.exceptions import ValidationError
# from django import forms
#
# def validate_alpha(value):
#     if not value.isalpha():
#         raise ValidationError("Input Must contain only alphabetical characters!")


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'bio', 'books']