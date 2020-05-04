from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    # path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]