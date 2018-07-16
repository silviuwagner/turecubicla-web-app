from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('<int:pk>/', views.PublicUserProfile.as_view(), name='public_profile'),
]