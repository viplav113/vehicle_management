from django.urls import path
from . import views
from .views import perform_quality_check


app_name = 'vehicles'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('add_vendor', views.add_vendor, name='add_vendor'),
    path('quality-check', views.perform_quality_check, name='quality_check'),

    # Add URLs for the new views you've implemented
    
    

    
]
