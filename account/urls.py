from django.urls import path
from .views import register, login
from .forms import UserRegistrationForm


urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login") 
]
