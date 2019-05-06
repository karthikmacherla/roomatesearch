from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import request
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models.query import EmptyQuerySet

from .forms import CustomUserCreationForm
from .forms import RoommateSurveyForm

from .algos import find_triadic_closures


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
    # get map data
    matches = find_triadic_closures(user)
    l = []
    for user, count in matches.items():
        l.append(user.first_name + " ")
        l.append(str(count) + "\n")
    return HttpResponse(''.join(l))


def roommate_survey(request):
    # user submitted the form
    if request.method == 'POST':
        form = RoommateSurveyForm(request.POST)
        if form.is_valid():
            form.process(request.user)
            return redirect('homepage')
    # otherwise, it's a get request so get the form
    user = request.user
    form = RoommateSurveyForm
    return render(request, 'homepage.html', {'form': form, 'user': user})