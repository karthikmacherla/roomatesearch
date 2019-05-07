from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Category
from django.core.exceptions import ObjectDoesNotExist

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('first_name', 'last_name', 'username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class RoommateSurveyForm(forms.Form):
    night_person = forms.BooleanField(label="Are you a night owl?", required=False)
    substances = forms.BooleanField(label="Do you partake in substances?", required=False)

    penn_college = forms.ChoiceField(choices=[
        ('seas', "Engineering"),
        ('sas', "Arts and Sciences"),
        ('nursing', "Nursing"),
        ('wharton', "Business")
    ])
    
    sport = forms.ChoiceField(choices=[
        ('tennis', "Tennis"),
        ('basketball', "Basketball"),
        ('football', "Football"),
        ('hockey', "Hockey")
    ])


    def helperGetObject(self, objects, key):
        try:
            obj = objects.get(pk=key)
            return obj
        except ObjectDoesNotExist:
            obj = Category(name=key)
            obj.save()
            return obj

    def process(self, user):
        data = self.cleaned_data
        categories = Category.objects

        # process data
        objects = []
        if data['night_person']:
            objects.append(self.helperGetObject(categories, 'night_person'))
        else:
            objects.append(self.helperGetObject(categories, 'morning_person'))
        
        if data['substances']:
            objects.append(self.helperGetObject(categories, 'substances'))
        else:
            objects.append(self.helperGetObject(categories, 'no_substances'))

        
        objects.append(self.helperGetObject(categories, data['penn_college']))


        objects.append(self.helperGetObject(categories, data['sport']))
        
        for obj in objects:
            obj.users.add(user)

