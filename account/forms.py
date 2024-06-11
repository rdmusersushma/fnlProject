from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = [
                'first_name',
                'last_name',
                'username',
                'password1',
                'password2',
                'email',
                "contact_number",
                "address",
                "bio",
                'is_student',
            ]


