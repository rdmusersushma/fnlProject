from django.db import models
from account.models import CustomUser
from django.utils import timezone

class StudentProfile(models.Model):
    additional_notes = models.TextField(blank=True,null=True)
    reg_no = models.CharField(max_length=10, primary_key=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
 
    def __str__(self):
        return f"{self.user_id.username}{self.reg_no}"
