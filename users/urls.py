from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('profile/trails/', views.UserProfileTrails.as_view(), name='profile_trails'),
    path('profile/settings/', views.UserProfileSettings.as_view(), name='profile_settings'),
    path('<int:pk>/', views.PublicUserProfile.as_view(), name='public_profile'),
]