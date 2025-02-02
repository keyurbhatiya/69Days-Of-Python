################################## Day 3: 69 Days of Python #####################################

# Python Booleans

# Booleans represent one of two values: True or False.

# Boolean Values
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# Example with if-else
a, b = 200, 33
print("b is greater than a" if b > a else "b is not greater than a")

# Evaluate Values and Variables
# The bool() function can evaluate the truth of a value
print(bool("Hello"))  # True
print(bool(15))       # True

# Most Values are True
print(bool("abc"))   # True
print(bool(123))     # True
print(bool(["apple", "cherry", "Mongo"]))  # True

# Some Values are False
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False

# Example with a class
class MyClass:
    def __len__(self):
        return 1

my_obj = MyClass()
print(bool(my_obj))  # True

# Functions can Return a Boolean
def my_function():
    return True

print(my_function())  # True

if my_function():
    print("YES!")
else:
    print("NO!")

# Python Operators
print(10 + 5)  # Example: Arithmetic addition

# Python Arithmetic Operators
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

# Python Assignment Operators
# =	x = 5
# +=	x += 3  (x = x + 3)
# -=	x -= 3  (x = x - 3)
# *=	x *= 3  (x = x * 3)
# /=	x /= 3  (x = x / 3)
# %=	x %= 3  (x = x % 3)
# //=	x //= 3 (x = x // 3)

# Python Comparison Operators
# ==	Equal
# !=	Not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to

# Python Logical Operators
# and, or, not

# Python Identity Operators
# is, is not

###################################### Python Lists ####################################

# Creating and Accessing Lists
my_list = ["apple", "Orange", "Mongo"]
print(my_list)            # Full list
print(my_list[0])         # Access by index
print(my_list[-1])        # Access last item
print(my_list[0:2])       # Access range of items
print(len(my_list))       # Length of list

# List Operations
list1, list2 = ["a", "b", "c"], ["d", "e", "f"]
print(list1 + list2)      # Concatenation
print(list1 * 2)          # Repetition

# Check if an Item Exists
if "Orange" in my_list:
    print("Yes, 'Orange' is in the list")

# List Methods
my_list.append("banana")          # Append an item
print(my_list)

my_list.insert(1, "grape")        # Insert an item
print(my_list)

my_list.remove("Mongo")           # Remove an item
print(my_list)

my_list.pop(1)                    # Remove item at index
print(my_list)

# Sorting and Reversing Lists
my_list = [3, 6, 1, 8, 2]
my_list.sort()                    # Sort in ascending order
print(my_list)

my_list.reverse()                 # Reverse the list
print(my_list)

# Clearing and Copying Lists
my_list = ["apple", "Orange", "Mongo"]
my_list.clear()                   # Clear all items
print(my_list)

my_list2 = my_list.copy()         # Copy the list
print(my_list2)

# Joining Lists
list3 = list1 + list2
print(list3)

# List Comprehension
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Looping Through Lists
for x in my_list:
    print(x)

for i in range(len(my_list)):
    print(my_list[i])

# List Methods Overview
# append()	Adds an element to the end
# clear()	Removes all elements
# copy()	Returns a copy of the list
# count()	Counts occurrences of a value
# extend()	Adds multiple elements
# index()	Returns the index of a value
# insert()	Adds an element at a position
# pop()	Removes the element at a position
# remove()	Removes the first occurrence
# reverse()	Reverses the order
# sort()	Sorts the list


###################################### Python Tuples ####################################

# Tuples Overview
# - Similar to lists, but immutable (cannot be changed after creation).
# - Defined using parentheses `()`.
# - Ordered, hashable, and memory-efficient.
# - Often used when values need to remain constant or as dictionary keys.
# - Commonly used for function return values or arguments.

# Example
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing Tuple Items
print(my_tuple[0])  # Output: apple

# Tuple Length
print(len(my_tuple))  # Output: 3

# Tuple Methods
# - count(): Returns the number of occurrences of a value.
# - index(): Returns the index of the first occurrence of a value.

# Tuple Operations
# 1. Concatenation
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "date")
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('apple', 'banana', 'cherry', 'date')

# 2. Repetition
tuple2 = tuple1 * 2
print(tuple2)  # Output: ('apple', 'banana', 'apple', 'banana')

# 3. Membership
print("apple" in my_tuple)  # Output: True

# Tuple Unpacking
x, y, z = my_tuple
print(x, y, z)  # Output: apple banana cherry

# Swapping Tuples
x = ("apple", "banana", "cherry")
y = ("orange", "mango", "grape")
x, y = y, x
print(x, y)

# Sorting a Tuple
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Output: ['apple', 'banana', 'cherry']

# Converting List to Tuple
fruits = ["apple", "banana", "cherry"]
tuple1 = tuple(fruits)
print(tuple1)  # Output: ('apple', 'banana', 'cherry')

# Looping Through a Tuple
# 1. Using `for`
for fruit in my_tuple:
    print(fruit)

# 2. Using `for` with index
for i in range(len(my_tuple)):
    print(my_tuple[i])

# 3. Using `while`
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

# Joining Two Tuples
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiplying Tuples
tuple2 = tuple1 * 2
print(tuple2)

# Tuple Methods Example
# - count()
print(my_tuple.count("apple"))  # Output: 1
# - index()
print(my_tuple.index("banana"))  # Output: 1
