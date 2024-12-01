################################## Day 8: 69 Days of Python #####################################

# Python Modules

# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module, you can save a Python script with a .py extension.
# Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)


# Use a Module
# To use a module, you can import it in your Python script.


# import mymodule

# mymodule.greeting("keyur")

# Variables in Module

# Save this code in the file mymodule.py
name = "keyur"


# import mymodule

# print(mymodule.name)


# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# import mymodule as keyur
# keyur.greeting("Kabir")


# Python Datetime

import datetime

x = datetime.datetime.now()
print(x)

# Date Output
# 2023-02-15 10:30:00.000000
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
import datetime

x = datetime.datetime.now()

print(x.strftime("%B"))

# The strptime() Method
# %A = weekday
# %B = month
# %d = day
# %m = month
# %Y = year
# %H = hour
# %M = minute
# %S = second
# %p = AM or PM


# Python Math
import math
# The math.ceil() Function
import math

print(math.ceil(1.4)) # 2

# The math.floor() Function
import math
print(math.floor(1.4)) # 1

# The math.pi Value
import math

print(math.pi) # 3.141592653589793

# The math.pow() Function
import math
print(math.pow(4, 3)) # 64

# The math.sqrt() Function
import math
print(math.sqrt(16)) # 4

# The math.fabs() Function
import math
print(math.fabs(-4.7)) # 4.7

# The math.factorial() Function
import math
print(math.factorial(5)) # 120

# The math.fsum() Function
import math
print(math.fsum([1, 2, 3, 4, 5])) # 15

# The math.gcd() Function
import math
print(math.gcd(48, 18)) # 6

#min() and max(),abs()
print(min(1, 2, 3, 4, 5)) # 1
print(max(1, 2, 3, 4, 5))  # 5
print(abs(-4.7)) # 4.7

# next topic python json ---> Day_9