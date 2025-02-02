################################## Day 9: 69 Days of Python #####################################

# Python JSON

"""
JSON (JavaScript Object Notation) is a syntax for storing and exchanging data.
It is text written with JavaScript object notation but can be used in Python.
"""
import json

# Parse JSON (Convert JSON string to Python object)
data = '{"name": "Keyur", "age": 20, "city": "Modasa"}'
parsed_data = json.loads(data)
print(parsed_data["age"])  # Output: 20

# Convert Python object to JSON string
python_data = {
    "name": "Keyur",
    "age": 20,
    "city": "Modasa"
}
json_data = json.dumps(python_data)
print(json_data)

# Converting different Python objects to JSON
print(json.dumps({"name": "Keyur", "age": 20}))  # dict
print(json.dumps(["apple", "banana"]))  # list
print(json.dumps(("apple", "banana")))  # tuple
print(json.dumps("Hello"))  # string
print(json.dumps(42))  # int
print(json.dumps(31.76))  # float
print(json.dumps(True))  # boolean
print(json.dumps(None))  # None

# More complex Python object
complex_data = {
    "name": "Keyur",
    "age": 20,
    "married": True,
    "children": ("Alice", "Nithya"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Formatting JSON output
print(json.dumps(complex_data, indent=4))  # Indented for readability
print(json.dumps(complex_data, indent=4, separators=(". ", " = ")))  # Custom separators
print(json.dumps(complex_data, indent=4, sort_keys=True))  # Sorted keys

################################## Python RegEx ####################################

"""
Regular Expressions (RegEx) are used to search, match, and manipulate text.
"""
import re

# Example: Search for the first whitespace character
text = "For only $1"
match = re.search("\\s", text)
print("First whitespace character at position:", match.start())

# RegEx Functions:
# 1. findall() - Returns a list of all matches
# 2. search() - Returns the first match object (or None if no match)
# 3. split() - Splits string into a list by matches
# 4. sub() - Replaces matches with a specified string

# findall()
text = "The rain in Spain"
matches = re.findall("ai", text)
print(matches)  # Output: ['ai', 'ai']

# search()
match = re.search("\\s", text)
print("First whitespace character at position:", match.start())

# split()
split_text = re.split("\\s", text)
print(split_text)  # Output: ['The', 'rain', 'in', 'Spain']

# sub()
replaced_text = re.sub("\\s", "9", text)
print(replaced_text)  # Output: The9rain9in9Spain

# Match Object
match = re.search("ai", text)
if match:
    print("Match span:", match.span())  # Tuple of start and end positions
    print("Original string:", match.string)  # Original string passed to re.search
    print("Matched group:", match.group())  # Matched text

################################## Python PIP ####################################

"""
PIP is a package manager for Python packages.
"""

# Check PIP version
# Run in terminal: pip --version

# Install a package
# Run in terminal: pip install numpy

# List installed packages
# Run in terminal: pip list

# Example using numpy
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)  # Output: [1 2 3 4 5]


#Python Try Except ---> Day_10