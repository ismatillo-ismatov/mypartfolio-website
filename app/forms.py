from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post,Profile


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    widgets = {
        'tag':forms.CheckboxSelectMultiple(),
    }

class UserForm(ModelForm):
    class Meta:
        model = User        
        fields = ['first_name','last_name','email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']