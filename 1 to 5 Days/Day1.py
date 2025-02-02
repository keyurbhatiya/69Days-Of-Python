# Day 1: 69 Days of Python

# Python Syntax
print("Day 1: 69 Days of Python")

# Python Indentation
if 5 > 2:
    print("Five is greater than two!")

# Python Variables
x = 50
y = "Hello, Keyur!"
print(x)
print(y)

# Comments
# This is a single-line comment in Python

# Multiline Comments
"""
This is a multiline comment in Python,
written over multiple lines.
"""

# Creating Variables
x = 5
y = "Keyur!"
print(x)
print(y)

# Casting
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

# Get the Type
x = 5
y = "Keyur!"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

# Single or Double Quotes
x = "Hello"  # Same as
x = 'Hello'

# Case-Sensitive
a = 4
A = "Sally"
# `A` will not overwrite `a`
print(a, A)

# Variable Names
myvar = "Keyur!"
my_var = "Keyur!"
_my_var = "Keyur!"
myVar = "Keyur!"
MYVAR = "Keyur!"
myvar2 = "Keyur!"

# Multi-Word Variable Names

# Camel Case
myVariableName = "Keyur!"

# Pascal Case
MyVariableName = "Keyur!"

# Snake Case
my_variable_name = "Keyur!"

# Assigning Multiple Values

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = " Keyur!"
print("Python is Awesome!" + x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Global Variables
x = "great for everyone who wants to learn Python"

def myfunc():
    print("Python is " + x)

myfunc()

# The global Keyword
x = "global"

def myfunc():
    global z
    z = "great for everyone who wants to learn Python Programming"

myfunc()

print("Python is " + z)
