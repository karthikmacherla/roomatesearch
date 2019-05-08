from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# User Model based on Django's build in model
# Framework gives parameters for username, first name, last name, 
# and their potential roomate.


class CustomUser(AbstractUser):
	partner = models.OneToOneField('CustomUser', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

# Category Model that represents choices the user makes. Ex. Category for 
# people who are night people or drink. 

class Category(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)

# Group model that allows users to create their own group based on people they know
# Still required to fill out the form, but now the group allows them to match 
# themselves within the group they filled out. 
class Group(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	users = models.ManyToManyField(CustomUser)
	owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='group_owned')
