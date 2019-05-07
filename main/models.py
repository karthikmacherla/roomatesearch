from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Category(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)

class Group(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)
