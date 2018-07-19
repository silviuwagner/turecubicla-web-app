from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	about = models.TextField(max_length=500,default="Câteva cuvinte depsre tine...")
	age = models.PositiveIntegerField(default=18)
	location = models.CharField(max_length=50,default="România")
	bike = models.CharField(max_length=50,default="Bicicleta favorită...")