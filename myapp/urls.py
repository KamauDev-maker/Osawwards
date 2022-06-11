from django.urls import include,path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/',include('django.contrib.auth.urls'), name='account'),
    path('profile/<username>', views.profile, name='profile'),
    path('<username>/profile',views.user_profile, name='user_profile'),    
    path('profile/<username>/settinga', views.edit_profile, name='edit'), 
    path('project/<post>',views.projectView,name='project'),    
    path('search/',views.search_project,name='search'), 
]

