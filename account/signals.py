from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from .models import CustomUser
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_profile_on_user_save(sender, instance, created, **kwargs):
    if created:
        user_type = kwargs.get('user_type')  # Access user type from kwargs
        if user_type == 'teacher':
            Teacher.objects.create(user=instance)
        elif user_type == 'student':
            Student.objects.create(user=instance)
        else:
            raise ValueError('Invalid user type provided.')

