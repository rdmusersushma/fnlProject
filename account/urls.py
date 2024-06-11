from django.urls import path
from .views import register
from .forms import UserRegistrationForm


urlpatterns = [
    path('register/', register, name="register") 
]
