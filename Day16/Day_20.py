################################## Day 20: 69 Days of Python #####################################

# Django Template Variables

# templates/template.html
'''
<h1>Hello {{ firstname }}, how are you?</h1>
'''

# Create Variable in View
'''
views.py:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))
'''

# Create Variables in Template
'''
{% with firstname="Tobias" %}
<h1>Hello {{ firstname }}, how are you?</h1>
{% endwith %}
'''

# Data From a Model
'''
members/views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
'''

# Template Tags
'''
templates/template.html:

{% if greeting == 1 %}
  <h1>Hello</h1>
{% else %}
  <h1>Bye</h1>
{% endif %}
'''

# Django Code
'''
templates/template.html:

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>
'''

# Tag Reference
'''
autoescape -->  Specifies if autoescape mode is on or off
block	--> Specifies a block section
comment	--> Specifies a comment section
csrf_token	--> Protects forms from Cross Site Request Forgeries
cycle	--> Specifies content to use in each cycle of a loop
debug	--> Specifies debugging information
extends	--> Specifies a parent template
filter	--> Filters content before returning it
firstof	--> Returns the first not empty variable
for	--> Specifies a for loop
if	--> Specifies a if statement
ifchanged	--> Used in for loops. Outputs a block only if a value has changed since the last iteration
include	--> Specifies included content/template
load	--> Loads template tags from another library
lorem	--> Outputs random text
now	--> Outputs the current date/time
regroup	--> Sorts an object by a group
resetcycle	--> Used in cycles. Resets the cycle
spaceless	--> Removes whitespace between HTML tags
templatetag	--> Outputs a specified template tag
url	Returns --> the absolute URL part of a URL
verbatim	--> Specifies contents that should not be rendered by the template engine
widthratio	--> Calculates a width value based on the ratio between a given value and a max value
with	--> Specifies a variable to use in the block
'''

# If Statement
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% endif %} 

# Elif
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% elif greeting == 2 %}
#   <h1>Bye</h1>
# {% endif %}

# Else
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% else %}
#   <h1>Bye</h1>
# {% endif %}

# Operators
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% elif greeting == 2 %}
#   <h1>Bye</h1>
# {% elif greeting == 3 %}
#   <h1>Goodbye</h1>
# {% else %}
#   <h1>Default</h1>
# {% endif %}


# For Loops
# {% for x in fruits %}
#   <h1>{{ x }}</h1>
# {% endfor %}

# Data From a Model
# {% for x in mymembers %}
#   <li>{{ x.firstname }} {{ x.lastname }}</li>
# {% endfor %}


# Reversed
# {% for x in members reversed %}
#   <h1>{{ x.id }}</h1>
#   <p>
#     {{ x.firstname }}
#     {{ x.lastname }}
#   </p>
# {% endfor %}  


# Empty
# <ul>
#   {% for x in emptytestobject %}
#     <li>{{ x.firstname }}</li>
#   {% empty %}
#     <li>No members</li>
#   {% endfor %}
# </ul> 

# Loop Variables
# Django has some variables that are available for you inside a loop:

# forloop.counter
# forloop.counter0
# forloop.first
# forloop.last
# forloop.parentloop
# forloop.revcounter
# forloop.revcounter0


# forloop.counter
# forloop.counter0
# forloop.first
# forloop.last
# forloop.parentloop
# forloop.revcounter
# forloop.revcounter0

# {% for x in mymembers %}
#   <li>
#     {{ forloop.counter }}
#     {{ forloop.counter0 }}
#     {{ forloop.first }}
#     {{ forloop.last }}
#     {{ forloop.parentloop }}
#     {{ forloop.revcounter }}
#     {{ forloop.revcounter0 }}
#   </li>
# {% endfor %}



# Comments
# <h1>Welcome Everyone</h1>
# {% comment %}
#   <h1>Welcome ladies and gentlemen</h1>
# {% endcomment %}


# Comment Description
# <h1>Welcome Everyone</h1>
# {% comment "This is a comment" %}
#   <h1>Welcome ladies and gentlemen</h1>
# {% endcomment %}

# Smaller Comments
# <h1>Welcome{# Everyone#}</h1>


# Django include Tag
# {% include 'base.html' %}


'''Next Topic Django QuerySets ---> Day_21.py'''