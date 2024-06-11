from django.forms import ModelForm
from .models import TeacherProfile

class TeacherRegistrationForm(ModelForm):
    class Meta:
        model = TeacherProfile
        fields = [
            "department",
            "position",
            "qualifications",
            "subjects_teaching",
            "years_of_experience",
            "additional_notes",
            "date_posted",
        ]
