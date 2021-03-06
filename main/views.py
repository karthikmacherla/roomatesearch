from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import request
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models.query import EmptyQuerySet
from django.contrib.auth import logout

from .forms import CustomUserCreationForm
from .forms import RoommateSurveyForm

from .algos import find_triadic_closures
from .algos import pair_group
from .algos import find_pairs_in_group


# constant for threshold for recommending someone
MATCH_THRESHOLD = 3

# This is a signup view for creating an account 
# on our application. 
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# This view redirect a logged in user to their homepage. 
# A homepage can either be the roommate form, a status of their potential roommate,
# or a screen showing those in their group. 

def homepage(request):
    # redirects to form or home depending on if user has filled out form before
    user = request.user
    # if user is not logged in or already has the attribute
    if user == None or not user.is_authenticated:
        return redirect('landing')
    elif user.category_set.count() > 0:
        return redirect('dashboard')
    else:
        return redirect('survey')

# This view defines the dashboard, showing their future roommate status.
# Finds the number of triadic closures between other users in any given time,
# then returns the nunber of matches.
def dashboard(request):
    user = request.user
    # case 1: this person's in a group
    if user.group_set.count() > 0:
        group = list(user.group_set.all())[0] # get group this user is in
        if group.matched:
            return match_view(request)
        return render(request, 'homepage.html', {'group': group, 'user': user})
    # get map data
    matches = find_triadic_closures(user)
    # filter matches based on threshold
    filtered = {k: v for k,v in matches.items() if v >= MATCH_THRESHOLD and k != user}
    return render(request, 'homepage.html', {'matches': filtered, 'user': user})

# This view renders the survey. It then checks whether a form submission is valid. 

def roommate_survey(request):
    # user submitted the form
    if request.method == 'POST':
        form = RoommateSurveyForm(request.POST)
        if form.is_valid():
            form.process(request.user)
            return redirect('homepage')
    # otherwise, it's a get request so get the form
    else:
        form = RoommateSurveyForm
    user = request.user
    return render(request, 'homepage.html', {'form': form, 'user': user})

# This view lets users log out of the app

def logout_view(request):
    logout(request)
    return redirect('homepage')

# Defines who their potential match is

def match_view(request):
    user = request.user
    group = list(user.group_set.all())[0] # get group this user is in

    if group.matched == False:
        pair_group(group) # pair everyone
    
    # find all pairs and show it
    pairs = find_pairs_in_group(group)
    return render(request, 'homepage.html', {'group': group, 'pairs': pairs, 'user': user})