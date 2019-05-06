from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import RoommateSurvey

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('first_name', 'last_name', 'username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class RoommateSurveyForm(forms.ModelForm):

    class Meta:
        model = RoommateSurvey
        fields = [
            'do_you_drink',
            'do_you_smoke', 
            'are_you_sporty',
            'do_you_game',
            'type_of_gamer',
        ]