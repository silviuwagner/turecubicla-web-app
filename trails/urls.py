from django.urls import path, include
from . import views
from rest_framework import routers

router =  routers.DefaultRouter()
router.register('trails', views.TrailView)

urlpatterns = [
     path('', views.TrailListView.as_view(), name='trail_list'),
     path('my/', views.UserTrailsView.as_view(), name='user_trails'),
	path('new/', views.TrailCreateView.as_view(), name='trail_new'),
	path('<int:pk>/edit/',
         views.TrailUpdateView.as_view(), name='trail_edit'),
     path('<int:pk>/',
         views.TrailDetailView.as_view(), name='trail_detail'),
     path('<int:pk>/delete/',
         views.TrailDeleteView.as_view(), name='trail_delete'),
     path('api/', include(router.urls)),
]