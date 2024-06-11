from django.forms import ModelForm
from .models import StudentProfile

class StudentRegistrationForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            "additional_notes",
            "reg_no",
            "date_posted",
        ]
