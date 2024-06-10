from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import urls

def shome(request):
	return render(request, 'student/student_dashboard.html')
	

def sregister(request):
#	if request.method = 'POST':
#		from = UserRegisterForm(request.POST)
#		if form.is_valid():
#			form.save()
#			username = form.cleaned_data.get('username')
#			messages.successs(request, f'Your account has been created ! You are now able to log in')
#			return redirect('login')
#	else:
#		from = UserRegisterForm()
	return render(request, 'student/sregister.html')
	

def slogin(request):
	return render(request, 'student/slogin.html')

@login_required
def sprofile(request):
	return render(request, 'student/sprofile.html')
	
# Create your views here.
