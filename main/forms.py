from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Category
from .models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

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
    substances = forms.BooleanField(label="Do you partake in substances?")

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

    
    # get the choices
    # TODO: change to 2 CharFields, one for creating group, one for joining
    join_group = forms.CharField(max_length=50, required=False, empty_value=None)
    create_group = forms.CharField(max_length=50, required=False, empty_value=None)

    # custom validation for group fields
    def clean(self):
        form_data = self.cleaned_data
        join_group = form_data['join_group']
        create_group = form_data['create_group']

        # can't join and create a group at the same time
        if join_group != None and create_group != None:
            self._errors['join_group'] = ['Either create group or join group']
            del join_group
            del create_group
        else:
            if join_group != None:
                if not Group.objects.filter(pk=join_group).exists():
                    self._errors['join_group'] = ['This group does not exist']
                    del join_group
            
            # make sure group you want to create does not exist
            if create_group != None:
                if Group.objects.filter(pk=create_group).exists():
                    self._errors['create_group'] = ['This group already exists']
                    del create_group
        
        return form_data


    def helper_get_category(self, objects, key):
        try:
            obj = objects.get(pk=key)
            return obj
        except ObjectDoesNotExist:
            obj = Category(name=key)
            obj.save()
            return obj

    def helper_get_group(self, objects, key):
        try:
            obj = objects.get(pk=key)
            return obj
        except ObjectDoesNotExist:
            obj = Group(name=key)
            return obj

    def process(self, user):
        data = self.cleaned_data
        categories = Category.objects

        # process data
        objects = []
        if data['night_person']:
            objects.append(self.helper_get_category(categories, 'night_person'))
        else:
            objects.append(self.helper_get_category(categories, 'morning_person'))
        
        if data['substances']:
            objects.append(self.helper_get_category(categories, 'substances'))
        else:
            objects.append(self.helper_get_category(categories, 'no_substances'))

        
        objects.append(self.helper_get_category(categories, data['penn_college']))

        objects.append(self.helper_get_category(categories, data['sport']))
        
        if data['join_group'] != None:
            groups = Group.objects
            objects.append(groups.get(pk=data['join_group']))
        elif data['create_group'] != None:
            groups = Group.objects
            objects.append(Group(name=data['create_group']))
        
        for obj in objects:
            obj.save()
            obj.users.add(user)
            obj.save()

