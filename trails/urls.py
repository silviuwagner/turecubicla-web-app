from django.urls import path

from . import views

urlpatterns = [
	path('', views.TrailListView.as_view(), name='trail_list'),
	path('new/', views.TrailCreateView.as_view(), name='trail_new'),
	path('<int:pk>/edit/',
         views.TrailUpdateView.as_view(), name='trail_edit'),
    path('<int:pk>/',
         views.TrailDetailView.as_view(), name='trail_detail'),
    path('<int:pk>/delete/',
         views.TrailDeleteView.as_view(), name='trail_delete'),
]