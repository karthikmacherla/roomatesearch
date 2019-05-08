from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('survey/', views.roommate_survey, name='survey'),
    path('logout/', views.logout_view, name='logout'),
    path('match/', views.match_view, name='match' ),
]