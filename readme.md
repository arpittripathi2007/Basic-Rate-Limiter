CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Recommended modules
 * Installation
 * Configuration

INTRODUCTION
------------

A simple rate limiter application in Django using Database Cache.

REQUIREMENTS
------------

Django and Sqllite and Cache
If you want to run inside django server we can create superuser directly
We can opt for PostMan

Installation
------------

``` pip install virtualenv ```

Install other packages from the requirements.txt after activating the virtualenv, though installing virtualenv is optional

CONFIGURATION
------------
 
   * ``` python3 -m venv venv ``` (Optional)
   * ``` source venv/bin/activate ```  (Optional)
   * ``` source venv/Scripts/activate ```  (Optional)
   * ``` pip install -r requirements.txt ``` 
   * ``` python manage.py makemigrations ```
   * ``` python manage.py makemigrations handlers```
   * ``` python manage.py migrate ```
   * ``` python manage.py createsuperuser -> admin ```
   * ``` python manage.py createsuperuser -> user1 ```(Optional)
   * ``` python manage.py createsuperuser -> user2 ```(Optional)
   * ``` python manage.py runserver ```

RUN
------------

First login into respective user (user created as superuser, for in-app running the application), Create Rate Limit Object per user per service(boundary and journey)

We can also register user using rest-api call preferably POST MAN
Set Authentication as basic-auth(if not login inside application) and give some parameter inside body of the request

URLs and Description

URLs  | Description
------------- | -------------
http://127.0.0.1:8000/admin  | Admin page, edit the data
http://127.0.0.1:8000/api/v1/journey  | Displays the response when user is hitting the url
http://127.0.0.1:8000/api/v1/journey/reset  | Reset cache data of journey type of user
http://127.0.0.1:8000/api/v1/boundary  | Displays the response when user is hitting the url
http://127.0.0.1:8000/api/v1/boundary/reset  | Reset cache data of boundary type of user
http://127.0.0.1:8000/api/v1/clear  | Clears all the data from cache
http://127.0.0.1:8000/api/v1/users  | Shows all the users
http://127.0.0.1:8000/api/v1/register  | Register the user
