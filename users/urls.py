from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile_edit/', views.UserProfile.as_view(), name='profile_edit'),
    path('<int:pk>/', views.PublicUserProfile.as_view(), name='public_profile'),
]