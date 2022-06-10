from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,PostForm,UpdateUserForm,UpdateUserProfileForm,RatingForm
from .models import Profile,Post,Rating
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import random


# Create your views here.


def  index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False )
            post.user = request.user
            post.save()
    else:
        form = PostForm()      
    try:
        posts = Post.objects.all()
        posts = posts[::-1]      
        a_post = random.randint(0, len(posts)-1)
        random_post = posts[a_post]
        print(random_post.photo)
        
    except post.DoesNotExist:
        posts=None

    return render(request, 'index.html', {'posts': posts,'form': form,'random_post': random_post})

def  signup(request):
    if request.method == 'POST':    
        form = SignupForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else: 
        form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})    
        

@login_required(login_url='login')   
def  profile(request,username):
    return render(request, 'profile.html')
        
@login_required(login_url='login')   
def  user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile',username=request.user.username)
    context = {
        'user_prof:user_prof,'
    }
    return render(request, 'userprofile.html', context)

@login_required(login_url='login') 
def  edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':    
        
       return render(request, 'editprofile.html',)
   
def  projectView(request,post):
    post =Post.objects.get(title=post)
    return render(request, 'project.html',)

def  search_project(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        results = Post.objects.filter(title_icontains=title).all()
        print(results)
        message = f'name'
        context = {
            'message': message, 
            'results': results
        }
        return render(request, 'results.html', context)
    else:
        messsage = 'No results found for the specified title'
        
    return render(request, 'results.html', {'messsage': messages})   
      
    
    
        