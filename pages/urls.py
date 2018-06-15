from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('story/', views.StoryPageView.as_view(), name='story'),
    path('team/', views.TeamPageView.as_view(), name='team'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]