from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class RoommateSurvey(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	do_you_drink = models.BooleanField()
	do_you_smoke = models.BooleanField()
	are_you_sporty = models.BooleanField()
	do_you_game = models.BooleanField()

	IPHONE_GAMES = 'iphone'
	FPS = 'fps'
	SUPER_SMASH = 'smash'
	NONE = 'na'
	GAME_CHOICES = (
		(IPHONE_GAMES, 'iPhone Games'),
		(FPS, 'First person shooter'),
		(SUPER_SMASH, 'Super Smash'),
		(NONE, 'None'),
	) 

	type_of_gamer = models.CharField(
		max_length = 10,
		choices = GAME_CHOICES, 
		default = IPHONE_GAMES
	)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name


