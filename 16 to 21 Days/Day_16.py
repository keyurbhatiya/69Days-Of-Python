################################## Day 16: 69 Days of Python #####################################

'''
Django is a back-end server side web framework.

Django is free, open source and written in Python.

Django makes it easier to build web pages using Python.
'''

# Installation of Django
# You can install Django using pip, which is Python's package manager.
# You can install it by running the following command in your terminal:
# pip install django

# Checking Django Version
# You can check the version of Django by running the following command in your terminal:
# python -c "import django; print(django.get_version())"

import django
print(django.get_version())

# Example
# <ul>
#   {% for x in mymembers %}
#     <li>{{ x.firstname }}</li>
#   {% endfor %}
# </ul>


'''
How does Django Work?
Django follows the MVT design pattern (Model View Template).

Model - The data you want to present, usually data from a database.
View - A request handler that returns the relevant template and content - based on the request from the user.
Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

The models are usually located in a file called models.py.

The views are usually located in a file called views.py.

The templates are usually located in a folder called templates.

When a user requests a URL, Django decides which view it will send it to.

This is done in a file called urls.py.
'''

# Virtual Environment
# You can create a virtual environment using the following command in your terminal:
# python -m venv env
# This creates a new environment named "env".
# You can activate the environment by running the following command in your terminal:
# .\env\Scripts\activate
# This activates the environment, and you can install packages using pip.



# Django Create Project
# You can create a new Django project using the following command in your terminal:
# django-admin startproject my_tennis_club

# Run the Django Project
# You can run the Django project by running the following command in your terminal:
# python manage.py runserver

# Create App
# py manage.py startapp members

# Views

# my_tennis_club/members/views.py :
'''from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")'''


#urls
'''from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]'''

#Template
'''
Create a templates folder inside the members folder, and create a HTML file named myfirst.html.

The file structure should be like this:

my_tennis_club
    manage.py
    my_tennis_club/
    members/
        templates/
            myfirst.html


'''
# <!DOCTYPE html>
# <html>
# <body>

# <h1>Hello World!</h1>
# <p>Welcome to my first Django project!</p>

# </body>
# </html>

# Modify the View
'''
Open the views.py file and replace the members view with this:

my_tennis_club/members/views.py:

from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
'''

# Change Settings

'''
This is done in the settings.py file in the my_tennis_club folder.

Look up the INSTALLED_APPS[] list and add the members app like this:

my_tennis_club/my_tennis_club/settings.py:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]
'''


# Then run this command:

# python manage.py runserver



# Create Table (Model)
'''
To create a model, navigate to the models.py file in the /members/ folder.

Open it, and add a Member table by creating a Member class, and describe the table fields in it:

my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
'''

# Migrate
# Navigate to the /my_tennis_club/ folder and run this command:

# py manage.py makemigrations members

# Run the migrate command:

# py manage.py migrate

# View SQL
# py manage.py sqlmigrate members 0001


''' Next topic: Django insert,update,delete --> Day_17.py '''