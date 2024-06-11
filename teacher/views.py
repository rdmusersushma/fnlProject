from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.forms import TeacherRegistrationForm
from . import urls

def thome(request):
	return render(request, 'teacher/teacher_dashboard.html')
	

def register(request):
    if request.method == "GET":
        form = TeacherRegistrationForm()
        return render(request, 'teacher/register.html', {'form': form})
    elif requset.method == "POST":
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success("successfully completed the user profile creation")
            return redirect("account/login")
    # if registering failed
    return redirect('teacher/register')
	

def tlogin(request):
	return render(request, 'teacher/tlogin.html')
	
@login_required
def tprofile(request):
	return render(request, 'teacher/tprofile.html')
	
# Create your views here.
