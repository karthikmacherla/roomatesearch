from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import request
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect

from .forms import CustomUserCreationForm
from .forms import RoommateSurveyForm
# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def homepage(request):
    # redirects to form or home depending on if user has filled out form before
    user = request.user
    # if user is not logged in or already not have the attribute
    if user == None or not user.is_authenticated or hasattr(user, 'roommatesurvey'):
        return redirect('landing')
    else:
        return redirect('survey')


def roommate_survey(request):
    # user submitted the form
    if request.method == 'POST':
        form = RoommateSurveyForm(request.POST)
        if form.is_valid():
            tmp = form.save(commit = False)
            tmp.user = request.user
            tmp.save()
            return redirect('/')
    # otherwise, it's a get request so get the form
    user = request.user
    form = RoommateSurveyForm
    return render(request, 'homepage.html', {'form': form, 'user': user})