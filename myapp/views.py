from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.


def  index(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    
def  profile(request,username):
    return render(request, 'profile.html')
        
    
def  user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile',username=request.user.username)
    context = {
        'user_prof:user_prof,'
    }
    return render(request, 'userprofile.html', context)

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
      
    
    
        