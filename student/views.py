from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.forms import StudentRegistrationForm

from . import urls

def shome(request):
	return render(request, 'student/student_dashboard.html')
	

def register(request):
    if request.method == "GET":
        form = StudentRegistrationForm()
        return render(request, 'student/register.html', {'form': form})
    elif request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success("successfully completed the user profile creation")
            return redirect("account/login")
    # if registering failed
    return redirect('student/register')



#	if request.method = 'POST':
#		from = UserRegisterForm(request.POST)
#		if form.is_valid():
#			form.save()
#			username = form.cleaned_data.get('username')
#			messages.successs(request, f'Your account has been created ! You are now able to log in')
#			return redirect('login')
#	else:
#		from = UserRegisterForm()
	

def slogin(request):
	return render(request, 'student/slogin.html')

@login_required
def sprofile(request):
	return render(request, 'student/sprofile.html')
	
# Create your views here.
