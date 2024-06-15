from django.urls import path
from . import views

urlpatterns = [
    path('sregister/', views.register,name='s-register'),
    path('shome/', views.shome, name='s-home'),
    path('slogin/', views.slogin, name ='s-login'),
    path('sprofile/', views.sprofile, name='s-profile'),
    
]

