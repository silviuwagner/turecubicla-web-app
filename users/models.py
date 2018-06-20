from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	about = models.TextField(max_length=500,default="A couple of words about yourself...")
	age = models.PositiveIntegerField(default=18)
	location = models.CharField(max_length=50,default="Country you live in...")
	bike = models.CharField(max_length=50,default="Your favorite bike...")