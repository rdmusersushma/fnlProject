from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from account.forms import UserRegistrationForm


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Successfully registered")
            if user.is_student:
                return redirect('/student/register')
            else:
                return redirect('/teacher/register')
