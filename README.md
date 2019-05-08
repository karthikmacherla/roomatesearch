# Roomate Search 

## About

This application, targeted towards Penn Students, allows users to sign-up, creating an account on our database, 
and match with potential roommates based on similar interests / qualities. Users fill out a form asking about 
qualities like whether you stay up late at night, and finds the user who fits the number of qualities you do.


## How it works

The application runs on Python + Django. Users sign up for an account, registering their account on our SQL-Lite
database, along with others. They then are presented with a form as shown below. 

The form places the user in certain foci groups (categories), that that are then compared to induce a focal closure
between the two users. The greater number of focal closures, the higher the recommendation. 


## Running this application

Download the project via zip or fork the repository. Run with the following command:

```
python manage.py runserver
```

Then open localhost:8000


## Demo of our Application


