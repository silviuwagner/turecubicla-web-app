from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(default=21)
	location = models.CharField(max_length=100)