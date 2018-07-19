from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
import trails.models

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class PublicUserProfile(TemplateView):
	model = models.CustomUser
	template_name = 'public_profile.html'

class UserProfile(LoginRequiredMixin, TemplateView):
	model = models.CustomUser
	template_name = 'user_profile.html'
	fields = ['about', 'age', 'location', 'bike']
	login_url = 'login'

class UserProfileTrails(LoginRequiredMixin, ListView):
	model = trails.models.Trail
	template_name = 'user_profile_trails.html'
	login_url = 'login'

class UserProfileSettings(LoginRequiredMixin, TemplateView):
	template_name = 'user_profile_settings.html'
	login_url = 'login'
	