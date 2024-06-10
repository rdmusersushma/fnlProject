from django.urls import path
from . import views

urlpatterns = [
    path('tregister/', views.tregister,name='t-register'),
    path('thome/', views.thome, name='t-home'),
    path('tlogin/', views.tlogin, name ='t-login'),
    path('tprofile/', views.tprofile, name='t-profile'),    
]

