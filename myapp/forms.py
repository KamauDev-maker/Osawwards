from django import forms
from django.contrib.auth.models import User
from django.contrrib.auth.forms import UserCreationForm
from .models import Post,Profile,Rating

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text="Required .Email address")
    
    class Meta:
        model = User
        