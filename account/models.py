from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=100, blank=True)
    is_student = models.BooleanField(default=False)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_pictures/',blank=True,null=True)
    address = models.TextField(null=True)
    contact_number = models.CharField(max_length=20,default='No contact number provided')
    GENDER_CHOICES =[
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
        ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    
    def __str__(self):
        return self.username
