from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,PostForm,UpdateUserForm,UpdateUserProfileForm,RatingForm
from .models import Profile,Post,Rating
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
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
        print(random_post)
    except Post.DoesNotExist:
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
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request. FILES,instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid:
            user_form.save()
            prof_form.save()
            return redirect('profile',user.usernme)
        
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'prof_form': prof_form,
    }         
        
    return render(request, 'editprofile.html',context)
 
 
@login_required(login_url='login')  
def  projectView(request,post):
    post =Post.objects.get(title=post)
    rating = Rating.objects.filter(user=request.user,post=post).first()
    rating_status = None
    if rating is None:
        rating_status = False
        
    else:
        rating_status = True
        
    if request.method == 'POST':
        form = RatingForm(request.POST) 
        if form.is_valid():
            rate = form.save(commit =False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Rating.objects.filter(post=post)
            
            design_ratings = [des.design for des in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [usa.usability for usa in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    
    else:
        form = RatingForm()
    context = {
        'post':post,
        'rating_status':rating_status,
        'rating_form':form,
    }       
           
    return render(request, 'project.html',context)

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
      

def logout_user(request):
    logout(request)
    return redirect('index')          
    
    
        