################################## Day 6: 69 Days of Python #####################################

# Python Functions

# Creating and Calling a Function
def greet(name):
    print(f"Hello, {name}")

greet("Keyur")

# Arguments and Multiple Calls
def display_surname(fname):
    print(f"{fname} Refsnes")

display_surname("Emil")
display_surname("Tobias")
display_surname("Linus")

# Multiple Arguments
def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name("Emil", "Refsnes")

# Arbitrary Arguments (*args)
def youngest_child(*kids):
    print(f"The youngest child is {kids[-1]}")

youngest_child("Emil", "Tobias", "Linus")

# Keyword Arguments
def youngest_named(child3, child2, child1):
    print(f"The youngest child is {child3}")

youngest_named(child1="Emil", child2="Tobias", child3="Linus")

# Arbitrary Keyword Arguments (**kwargs)
def person_details(**kwargs):
    print(f"He's {kwargs['age']} years old")

person_details(fname="John", lname="Doe", age="36")

# Default Parameter Value
def origin_country(country="Norway"):
    print(f"I am from {country}")

origin_country("Sweden")
origin_country("India")
origin_country()
origin_country("Canada")

# Passing a List
def display_items(items):
    for item in items:
        print(item)

fruits = ["apple", "banana", "cherry"]
display_items(fruits)

# Returning Values
def multiply_by_five(x):
    return 5 * x

print(multiply_by_five(3))
print(multiply_by_five(5))
print(multiply_by_five(9))

# The pass Statement
def placeholder_function():
    pass

# Positional-Only Arguments
def show_positional(x, /):
    print(x)

show_positional(3)

# Keyword-Only Arguments
def show_keyword(*, x):
    print(x)

show_keyword(x=3)

# Combine Positional-Only and Keyword-Only
def combine_arguments(a, b, /, *, c, d):
    print(a + b + c + d)

combine_arguments(5, 6, c=7, d=8)

############################### Python Lambda #################################

# Basic Lambda Function
add_ten = lambda a: a + 10
print(add_ten(5))

# Lambda with Multiple Arguments
add_three_numbers = lambda a, b, c: a + b + c
print(add_three_numbers(5, 6, 2))

# Lambda Inside a Function
def multiplier(n):
    return lambda a: a * n

double = multiplier(2)
print(double(5))

############################ Python Arrays #####################################

# Creating an Array
from array import array

int_array = array('i', [1, 2, 3, 4, 5])
print(int_array)

# Accessing Array Elements
string_array = ["Keyur", "Tutorial", "Python"]
print(string_array[1])

# Length of an Array
print(len(string_array))

# Looping Through an Array
for item in string_array:
    print(item)

# Adding and Removing Array Elements
string_array.append("Keyur")
print(string_array)

string_array.remove("Keyur")
print(string_array)

# Array Methods Example
data = [1, 2, 3, 4, 5]
data.extend([6, 7])
print("Extended Data:", data)
data.reverse()
print("Reversed Data:", data)
data.sort()
print("Sorted Data:", data)
