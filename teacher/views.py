from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from teacher.forms import TeacherRegistrationForm
from account.models import CustomUser
def thome(request):
	context ={
		'users':CustomUser.objects.all()
		}
	return render(request, 'teacher/teacher_dashboard.html',context)

@login_required
def register(request):
    if request.method == "GET":
        form = TeacherRegistrationForm()
        return render(request, 'teacher/tregister.html', {'form': form})
    elif request.method == "POST":
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            messages.success(request, "successfully completed the user profile creation")
            return redirect("login")
    # if registering failed
    return redirect('t-register')
	

def tlogin(request):
	return render(request, 'teacher/tlogin.html')
	
@login_required
def tprofile(request):
	return render(request, 'teacher/tprofile.html')
	
# Create your views here.
