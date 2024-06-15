from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from account.forms import UserRegistrationForm, UserLoginForm


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Successfully registered")
    #        login(user)
            if user.is_student:
                return redirect('s-register')
            else:
                return redirect('t-register')
            return redirect('/')
    return redirect('register')

def login(request):
    if request.method == "GET":
        form = UserLoginForm()
        return render(request, "account/login.html", {'form': form})
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password = password)
            if user:
                auth.login(request, user)
                messages.success(request, f"Hi, {username}, logged in Successfully")
                if user.is_student:
                    return redirect("s-profile")
                else:
                    return redirect("t-profile")
    return redirect("login")
