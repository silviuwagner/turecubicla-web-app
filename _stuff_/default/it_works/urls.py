from django.urls import path
from . import views

app_name = 'it_works'

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
