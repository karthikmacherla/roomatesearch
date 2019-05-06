from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('survey/', views.roommate_survey, name='survey'),
    path('thanks/', views.thanks, name='thanks')
]