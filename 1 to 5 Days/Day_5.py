################################## Day 5: 69 Days of Python #####################################

# Python If ... Else
# If-else statements execute different code blocks based on conditions.

# Syntax
# if condition:
#     # Code for true condition
# elif another_condition:
#     # Code for another true condition
# else:
#     # Code for all other cases

# Example
x, y = 33, 200
if y > x:
    print("y is greater than x")
elif x == y:
    print("x and y are equal")
else:
    print("x is greater than y")

# Short-hand If-Else
print("y is greater") if y > x else print("x is greater")

# Logical Operators
# 'and', 'or', 'not' combine or negate conditions.
a, b, c = 200, 33, 500
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one condition is True")
if not (a > c):
    print("a is NOT greater than c")

# Nested If
if a > b:
    if a > c:
        print("a is the greatest")
    else:
        print("a is greater than b but not c")
else:
    print("a is not greater than b")

# The pass Statement
# Used as a placeholder for future code.
if b > a:
    pass

################################# Python While Loop ####################################

# While Loops
# Repeats code while a condition is true.
i = 1
while i < 6:
    print(i)
    i += 1

# Break: Exit loop prematurely
# Continue: Skip current iteration
# Else: Executes after loop ends normally

i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

j = 0
while j < 6:
    j += 1
    if j == 3:
        continue
    print(j)

# While-Else Example
k = 1
while k < 6:
    print(k)
    k += 1
else:
    print("k is no longer less than 6")

##################################### Python For Loops ######################################

# For Loops
# Iterate over sequences like lists, tuples, dictionaries, sets, or strings.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Break: Exit loop prematurely
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# Continue: Skip current iteration
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Range Function
# Generate a sequence of numbers.
for num in range(2, 30, 3):
    print(num)

# For-Else Example
for num in range(6):
    print(num)
else:
    print("Loop completed!")

# Nested Loops
colors = ["red", "green", "blue"]
for color in colors:
    for fruit in fruits:
        print(color, fruit)

# Pass Statement
# Placeholder for future code.
for _ in range(10):
    pass
