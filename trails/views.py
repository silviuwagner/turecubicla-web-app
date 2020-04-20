from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import youtube_embed
from .filters import TrailFilter
from rest_framework import viewsets
from .serializers import TrailSerializer
from .models import Trail

class TrailView(viewsets.ModelViewSet):
	queryset = Trail.objects.all()
	serializer_class = TrailSerializer

class TrailCreateView(LoginRequiredMixin, CreateView):
	model = models.Trail
	template_name = 'trail_new.html'
	fields = ['title', 'about', 'region', 'distance', 'difficulty', 'image', 'track']
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class TrailListView(ListView):
	model = models.Trail
	template_name = 'trail_list.html'

	ordering = ['-date']
	paginate_by = 9

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = TrailFilter(self.request.GET, queryset=self.get_queryset())	
		return context

class TrailDetailView(DetailView):
	model = models.Trail
	template_name = 'trail_detail.html'

	# youtube_url = models.Trail.youtube_url

	# video_embed(youtube_url)

class TrailUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Trail
	fields = ['title', 'about', 'region', 'distance', 'difficulty', 'image', 'track', 'youtube_url']
	template_name = 'trail_edit.html'
	login_url = 'login'

class TrailDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Trail
	template_name = 'trail_delete.html'
	login_url = 'login'
	success_url = reverse_lazy('profile_trails')

class UserTrailsView(LoginRequiredMixin, ListView):
	model = models.Trail
	template_name = 'user_profile_trails.html'
	login_url = 'login'
	ordering = ['-date']

#success_url = reverse_lazy('trail_list')

# class AboutUsView(DetailView):
# 	template_name = 'about_us.html'