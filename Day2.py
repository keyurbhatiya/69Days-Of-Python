# Python Data Types

# Built-in Data Types

# Text Type = str
# Numeric Types = int, float, complex
# Sequence Types = list, tuple, range
# Mapping Type = dict
# Set Types = set, frozenset
# Boolean Type = bool
# Binary Types = bytes, bytearray, memoryview
# None Type = NoneType


### 1. Integers
x = 10
print(x)

### 2. Floats
x = 5.5
print(x)

### 3. Strings
x = "Hello"

# Getting the Data Type
print(type(x))

# Setting the Data Type
x = 50
x = int(x)
print(x)
print(type(x))

# Setting the Data Type
x = str(x)       
print(x)
print(type(x))

# Setting the Data Type
x = float(x)       
print(x)
print(type(x))


# Python Numbers

# Integers
x = 1    # int  
y = 2.8  # float
z = 1j   # complex


# Type Conversion


# Convert from int to float:      
# x = 1
a = float(x)
print(a)    
print(type(a))  

# Convert from float to int:  
# y = 2.8    
a = int(y)
print(a)    
print(type(a))

# Convert from int to complex:  
# x = 1
a = complex(x)
print(a)    
print(type(a))


# Random Number

import random

#Import the random module, and display a random number between 1 and 9:

print(random.randrange(1, 10)) # Return a random number between 1 and 9


# Python Casting is the process of converting a value of one data type to another data type.

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3  

print(x)
print(y)
print(z)


############################### Python Strings ##################################

# Strings in Python are enclosed in quotes.
# Strings are arrays of bytes representing unicode characters.
# Python supports the following string types: str, bytes, bytearray


# Strings
print("Hello, World!")
print('Hello, World!')


# Quotes Inside Quotes
print("Hello, 'Keyur'!")
print('Hello, "Keyur"!')
print('Hello, "Keyur"\'s Python Tutorial')

# Assign String to a Variable
x = "Hello, World!"
print(x)


# Multiline Strings
multi_line_string = """This is a multiline string with more than one line."""
print(multi_line_string)


# Strings are Arrays
# Strings are arrays of bytes representing unicode characters.
# You can access the string characters by referring to the index number.
# Remember that the first character has position 0.
# print("Hello, World!")
# print("H" + "e" + "l" + "l" + "o, " + "W" + "o" + "r" + "l" + "d" + "!")
# print("Hello, World!"[0])

a = "Hello, World!"
print(a[1])



# Looping Through a String
for x in "Python":  
    print(x)

# String Length
a = "Hello, Python!"
print(len(a))


# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"   
if "free" in txt:   
    print("Yes, 'free' is present.")

# Check if NOT
txt = "I Love Python!"
print("expensive" not in txt)

# Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])


# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])


# Python - Modify Strings

# Upper Case
a = "hello, keyur!"
print(a.upper())

# Lower case  
a = "HELLO, KEYUR!"
print(a.lower())

# Remove Whitespace
a = "   hello, keyur!   "   
print(a.strip())


# Replace String
a = "hello, keyur!"
print(a.replace("keyur", "python"))

# Split String
a = "hello, keyur!"
print(a.split(","))

# Python - String Concatenation

# String Concatenation
a = "Hello"
b = "Keyur!"
c = a + b
print(c)

# Python - Format - Strings

# String Formatting

age = 20
txt = "My name is Keyur, and I am {}"
print(txt.format(age))

# F-Strings

age = 20
txt = f"My name is Keyur, and I am {age} years old"
print(txt)

# Placeholders and Modifiers

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} INR."
print(myorder.format(quantity, itemno, price))


# Python - Escape Characters
# Escape Characters

# \n - New Line
# \r - Carriage Return
# \t - Horizontal Tab
# \\ - Backslash
# \f - Form Feed

txt = "Hello\nKeyur!"
print(txt)

txt = "Hello\rKeyur!"   
print(txt)  

txt = "Hello\tKeyur!"
print(txt)

txt = "Hello\\Keyur!"
print(txt)

txt = "Hello\fKeyur!"
print(txt)  


# Python - String Methods

# String Methods
# 1. capitalize() - Returns a copy of the string with the first character capitalized.
# 2. casefold() - Returns a casefolded copy of the string.
# 3. center(width[, fillchar]) - Returns a centered string of length width.
# 4. count(substring, start, end) - Returns the number of occurrences of substring in the range [start, end].
# 5. encode(encoding, errors) - Returns an encoded version of the string.
# 6. endswith(suffix, start, end) - Returns True if the string ends with the specified suffix, otherwise False.
# 7. expandtabs(tabsize=8) - Returns a copy of the string where all tab characters are expanded using spaces.
# 8. find(substring, start, end) - Returns the index of the first occurrence of substring in the range [start, end].
# 9. format(*args, **kwargs) - Returns a formatted version of the string.
# 10. format_map(mapping) - Returns a formatted version of the string.



