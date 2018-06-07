from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

class TrailCreateView(CreateView):
	model = models.Trail
	template_name = 'trail_new.html'
	fields = ['title', 'about', 'author', ]

class TrailListView(ListView):
	model = models.Trail
	template_name = 'trail_list.html'

class TrailDetailView(DetailView):
	model = models.Trail
	template_name = 'trail_detail.html'

class TrailUpdateView(UpdateView):
	model = models.Trail
	fields = ['title', 'about', ]
	template_name = 'trail_edit.html'

class TrailDeleteView(DeleteView):
	model = models.Trail
	template_name = 'trail_delete.html'

success_url = reverse_lazy('trail_list')