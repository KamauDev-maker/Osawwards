from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.profile, name='profile'),
    path('<username>/profile',viiews.user_profile, name='user_profile'),    
    path('profile/<username>/settinga', views.edit_profile, name='edit'), 
    path('project/<post>',views.projectView,name='project'),    
    path('search/',views.search_project,name='search'), 
]

