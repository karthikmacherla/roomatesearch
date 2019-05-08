from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
	def __str__(self):
		return self.first_name + ' ' + self.last_name

# pair of users
class Pair(models.Model):
	user1 = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="pair1")
	user2 = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="pair2")

class Category(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)

class Group(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)
	owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='group_owned')
	matched = models.BooleanField(default=False)
