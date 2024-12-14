################################## Day 21: 69 Days of Python #####################################


# Django QuerySets

# Querying Data

# Example
# views.py:

# from django.http import HttpResponse
# from django.template import loader
# from .models import Member

# def testing(request):
#   mydata = Member.objects.all()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# templates/template.html:

'''
<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>
'''
# The values() Method

'''
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
'''

# Return Specific Columns
'''
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.values_list('firstname')
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
'''

# Return Specific Rows
'''
from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.filter(firstname='Emil').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
'''

# QuerySet Filter
# mydata = Member.objects.filter(firstname='Emil').values()

# AND
# mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

# OR
# mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()


# Field Lookups
# Use the __startswith keyword:

# .filter(firstname__startswith='L');
# Is the same as the SQL statement:

# WHERE firstname LIKE 'L%'


# Order By
# mydata = Member.objects.all().order_by('firstname').values()


# Descending Order
# mydata = Member.objects.all().order_by('-firstname').values()


# Multiple Order Bys
# mydata = Member.objects.all().order_by('lastname', '-id').values()


# Django - Add Static File
'''
Add a CSS file in the static folder, the name is your choice, we will call it myfirst.css in this example

my_tennis_club
    manage.py
    my_tennis_club/
    members/
        templates/
        static/
            myfirst.css
'''

# my_tennis_club/members/static/myfirst.css
'''
body {
  background-color: lightblue;
  font-family: verdana;
}
'''

# Modify the Template
# {% load static %}
# <link rel="stylesheet" href="{% static 'myfirst.css' %}">


#exceple
# my_tennis_club/members/templates/template.html
'''
{% load static %}
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="{% static 'myfirst.css' %}">
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

</body>
</html>
'''


''' Next topic: Django PostgreSQL --> Day_22.py '''
