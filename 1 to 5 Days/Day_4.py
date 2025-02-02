################################## Day 4: 69 Days of Python #####################################

# Python Sets

# Sets are used to store multiple items in a single variable.
# Sets are unordered collections of unique elements.
# Sets are mutable, meaning they can be modified after creation.
# Sets are often used when we need to store a collection of items, but we don't care about the order of the items.
# Duplicates Not Allowed
# Sets are created using the set() function or the {} syntax.
# True and 1 is considered the same value

# Creating a Set
my_set = {1, 2, 3}
print(my_set) # Output: {1, 2, 3}

# Access Items
thisset = {"apple", "banana", "cherry"}
# Loop through the set, and print the values:
for x in thisset:
    print(x)    # Output: apple, banana, cherry

# Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # Output: True

# Check if "banana" is NOT present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) # Output: False

# Add Items
# Add an item to a set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

# Add multiple items to a set
my_set.update([5, 6, 7])
print(my_set) # Output: {1, 2, 3, 4, 5, 6, 7}

# Remove Item
my_set = {1, 2, 3, 4, 5, 6, 7}
my_set.remove(4)
print(my_set) # Output: {1, 2, 3, 5, 6, 7}

my_set.discard(5)
print(my_set) # Output: {1, 2, 3, 6, 7}

my_set.pop()
print(my_set) # Output: {2, 3, 6, 7}

my_set.clear()
print(my_set) # Output: set()

# del thisset removes the entire set.
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # NameError: name 'thisset' is not defined

# Join Sets
# Using union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # Output: {1, 2, 3, 'a', 'b', 'c'}

# Using update()
set1.update(set2)
print(set1) # Output: {1, 2, 3, 'a', 'b', 'c'}

# Using intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) # Output: {'apple'}

# Using difference()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.difference(set2)
print(set3) # Output: {'a', 'b', 'c'}

# Using symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # Output: {'banana', 'cherry', 'google', 'microsoft'}

################################# Python Dictionaries ####################################

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection of key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# Access Items
print(thisdict["brand"]) # Output: Ford
print(thisdict.get("model")) # Output: Mustang
print(thisdict.keys()) # Output: dict_keys(['brand', 'model', 'year'])
print(thisdict.values()) # Output: dict_values(['Ford', 'Mustang', 1964])
print(thisdict.items()) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Change Values
thisdict["year"] = 2018
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Adding Items
thisdict["color"] = "red"
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}

# Removing Items
thisdict.pop("model")
print(thisdict) # Output: {'brand': 'Ford', 'year': 2018, 'color': 'red'}

# Looping Through a Dictionary
for key in thisdict:
    print(key)  # Output: brand, year, color

for value in thisdict.values():
    print(value)  # Output: Ford, 2018, red

for key, value in thisdict.items():
    print(key, value)  # Output: brand Ford, year 2018, color red

# Copy a Dictionary
newdict = thisdict.copy()
print(newdict)

# Nested Dictionaries
family = {
  "child1": {
    "name": "Keyur",
    "year": 2004
  },
  "child2": {
    "name": "Yash",
    "year": 2006
  },
  "child3": {
    "name": "Om",
    "year": 2006
  }
}

print(family)
# Dictionary Methods
# - clear(): Removes all the elements from the dictionary.
# - fromkeys(): Returns a dictionary with the specified keys and value.
# - get(): Returns the value of the specified key.
# - items(): Returns a list containing a tuple for each key value pair.
# - keys(): Returns a list containing the dictionary's keys.
# - pop(): Removes the element with the specified key.
# - popitem(): Removes the last inserted key-value pair.
# - setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
# - update(): Updates the dictionary with the specified key-value pairs.
# - values(): Returns a list of all the values in the dictionary.

