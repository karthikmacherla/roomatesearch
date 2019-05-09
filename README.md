# Roomate Search 
http://karthikmacherla.pythonanywhere.com/

## About

This application, targeted towards Penn Students, allows users to sign-up, creating an account on our database, 
and match with potential roommates based on similar interests / qualities. Users fill out a form asking about 
qualities like whether you stay up late at night, and finds the user who fits the number of qualities you do.


## How it works

The application runs on Python + Django. Users sign up for an account, registering their account on our SQL-Lite
database, along with others. They then are presented with a form.  

Based on the form responses, a social affiliation network is created with edges between users and their favorite TV show, favorite sport, etc. Then, they get recommended matches in order of how many focal closures they have with each person

![Alt text](screenshots/image2.png?raw=true "Matches")

It also gives users the option of making/joining a group. The person who makes the group is the "owner," and once they are satisfied with the graph, they can click the "match" button and everyone in the group will be paired up, maximizing the total number of focal closures, thus providing an approximation of an optimal matching.

![Alt text](screenshots/image1.png?raw=true "group1")
![Alt text](screenshots/image3.png?raw=true "group2")



