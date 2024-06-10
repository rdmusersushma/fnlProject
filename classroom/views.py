from django.shortcuts import render


def home(request):
	return render(request,'classroom/home.html')

def about(request):
	return render(request, 'classroom/about.html')
# Create your views here.
