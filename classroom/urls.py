from django.urls import path
from . import views


urlpatterns = [
	path('',views.home, name='cs-home'),
	path('about/',views.about, name='cs-about'),
]
