from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	partner = models.OneToOneField('CustomUser', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Category(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)

class Group(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)
	owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='group_owned')
