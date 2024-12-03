################################## Day 10: 69 Days of Python #####################################

# Python Try Except
'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

# Exception Handling
try:
  print(x)
except:
  print("An exception occurred") # This statement will raise an error, because x is not defined


# Many Exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally
try:
  print("Hey!")
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# Example
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


# Python User Input
'''
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

Python 2.7 uses the raw_input() method.
'''

# Python 3.6
''' username = input("Enter username:")
print("Username is: " + username) '''

#Python 2.7
''' username = raw_input("Enter username:")
print("Username is: " + username) '''

# Python String Formatting
# format()

age = 20
txt = "My name is Keyur, I am {}"
print(txt.format(age))

# F-Strings
name = "Keyur"
txt = f"Python Tutorial by {name}"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} INR"
print(txt)

# Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} INR."
print(myorder.format(quantity, itemno, price))

# Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} INR."
print(myorder.format(quantity, itemno, price))

# Named Indexes
quantity = 3
itemno = 567
price = 49
myorder = "I want {quantity} pieces of item number {itemno} for {price:.2f} INR."
print(myorder.format(quantity=quantity, itemno=itemno, price=price))




########################### Excerices ###########################################

# create a simple calculator program using Python, capable of performing arithmetic operations such as addition, 
# subtraction, multiplication, and division.


# Next Topic File Handling --> Day 11