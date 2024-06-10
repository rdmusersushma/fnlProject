from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import urls

def thome(request):
	return render(request, 'teacher/teacher_dashboard.html')
	

def tregister(request):
#	if request.method = 'POST':
#		from = UserRegisterForm(request.POST)
#		if form.is_valid():
#			form.save()
#			username = form.cleaned_data.get('username')
#			messages.successs(request, f'Your account has been created ! You are now able to log in')
	return render(request, 'teacher/tregister.html')
	

def tlogin(request):
	return render(request, 'teacher/tlogin.html')
	
@login_required
def tprofile(request):
	return render(request, 'teacher/tprofile.html')
	
# Create your views here.
