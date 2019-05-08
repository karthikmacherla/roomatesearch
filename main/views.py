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


# constant for threshold for recommending someone
MATCH_THRESHOLD = 3

# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

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

def dashboard(request):
    user = request.user
    # case 1: this person's in a group
    if user.group_set.count() > 0:
        group = list(user.group_set.all())[0] # get group this user is in
        return render(request, 'homepage.html', {'group': group, 'user': user})
    # get map data
    matches = find_triadic_closures(user)
    # filter matches based on threshold
    filtered = {k: v for k,v in matches.items() if v >= MATCH_THRESHOLD and k != user}
    return render(request, 'homepage.html', {'matches': filtered, 'user': user})


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


def logout_view(request):
    logout(request)
    return redirect('homepage')

def match_view(request):
    user = request.user
    group = list(user.group_set.all())[0] # get group this user is in
