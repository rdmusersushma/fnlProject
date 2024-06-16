from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TeacherRegistrationForm, TeacherProfileUpdateForm
from account.forms import  UserUpdateForm
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
	if request.method == 'POST':
		user_profile = request.user.teacherprofile  # Assuming you have a OneToOne relation
		form = TeacherProfileUpdateForm(request.POST, instance=user_profile)  # Pre-populate with current data
		if form.is_valid():
			form.save()
			# Success message or redirect to profile page (optional)
			return redirect('t-profile')  # Replace with your profile URL name
		else:
			pass

	else:
		user_profile = request.user.teacherprofile
		form = TeacherProfileUpdateForm(instance=user_profile)  # Pre-populate with current data
	context = {'form': form}

	return render(request, 'teacher/tprofile.html', context)


#def update_profile(request):
#    if request.method == 'POST':
#        user_profile = request.user.TeacherProfile  # Assuming you have a OneToOne relation
#        form = TeacherProfileUpdateForm(request.POST, instance=user_profile)  # Pre-populate with current data
#        if form.is_valid():
#            form.save()
#            # Success message or redirect to profile page (optional)
#            return redirect('t-profile')  # Replace with your profile URL name
#    else:
#        user_profile = request.user.teacherprofile
#        form = TeacherProfileUpdateForm(instance=user_profile)  # Pre-populate with current data
#
#    context = {'form': form}
#    return render(request, 'update_profile.html', context)	
# Create your views here.
