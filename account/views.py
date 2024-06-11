from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from account.forms import UserRegistrationForm, UserLoginForm


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    elif request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Successfully registered")
            login(user)
            if user.is_student:
                return redirect('/student/register')
            else:
                return redirect('/teacher/register')
            return redirect('/')
    return redirect('/account/register')

def login(request):
    if request.method == "GET":
        form = UserLoginForm()
        return render(request, "account/login.html", {'form': form})
    elif request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password = password)
            if user:
                auth.login(request, user)
                messages.success(request, f"Hi, {username}, logged in Successfully")
                if user.is_student:
                    return redirect("student/profile")
                else:
                    return redirect("teacher/profile")
    return redirect("account/login")
