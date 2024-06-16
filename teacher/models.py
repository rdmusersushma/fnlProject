from django.db import models
from django.utils import timezone
from account.models import CustomUser

# Create your models here.
class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    qualifications = models.TextField(default = 'No adderss provided')
    subjects_teaching = models.CharField(max_length=255,null=True)
    years_of_experience = models.IntegerField(null=True)
    additional_notes = models.TextField(blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
#    user_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
 
    def __str__(self):
        return f'{self.user_id.username} Profile'
