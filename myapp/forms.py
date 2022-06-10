from django import forms
from django.contrib.auth.models import User
from django.contrrib.auth.forms import UserCreationForm
from .models import Post,Profile,Rating

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text="Required .Email address")
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        
class PostForm(forms.ModelForm):
    image =Imagefield(labe='')
    
    class Meta:
        model = Post
        fields = ('image', 'title', 'description', 'url','technologies')
        
class UpdateUserForm(forms.ModelForm):
      email = models.EmailField(max_length=255,help_text="Email address")
      
      class Meta:
          model = User
          fields = ('email', 'username')    
          
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'location', 'profile_image','bio','email')    
        
                
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content')         
          