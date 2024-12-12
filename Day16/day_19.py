################################## Day 19: 69 Days of Python #####################################

# Django Admin

# py manage.py runserver
# In the browser window, type 127.0.0.1:8000/admin/ in the address bar.


# Create User
# This is done by typing this command in the command view:

# py manage.py createsuperuser
'''
py manage.py createsuperuser
Username (leave blank to use 'keyur'): keyur
Email address: keyur@gmail.com
Password: 
Password (again): 
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''
# Now start the server again and login Now.


# Include Member in the Admin Interface
# my_tennis_club/members/admin.py:
'''
from django.contrib import admin
from .models import Member

# Register your models here.
admin.site.register(Member)
'''


# Change the String Representation Function

# my_tennis_club/members/models.py
'''
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
'''

# Set list_display
# my_tennis_club/members/admin.py
'''
from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)
'''


# Update Members
# Click the first member, keyur, to open the record for editing, and give him a joined_date



# Add Members
# To add a new member, click on the "ADD MEMBERS" button in the top right corner


# Delete Members
# To delete a new member, you can either select a member and choose the action "Delete selected members" 


''' Next Topic Django Template Variables ---> Day_20 '''