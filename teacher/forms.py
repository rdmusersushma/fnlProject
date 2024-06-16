from django.forms import ModelForm
from .models import TeacherProfile
from account.models import CustomUser
from django import forms

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


class TeacherProfileUpdateForm(forms.ModelForm):
        class Meta:
                model = TeacherProfile
                fields = ('department', 'position', 'qualifications',
                  'subjects_teaching', 'years_of_experience',
                  'additional_notes')

