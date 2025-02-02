################################## Day 10: 69 Days of Python #####################################

# Python Try-Except
"""
- `try` block tests a block of code for errors.
- `except` block handles the error.
- `else` block executes code if no errors occur.
- `finally` block executes code regardless of the try-except result.
"""

# Exception Handling
try:
    print(x)
except Exception as e:
    print(f"An exception occurred: {e}")

# Handling Specific Exceptions
try:
    print(x)
except NameError:
    print("Variable 'x' is not defined")
except:
    print("Something else went wrong")

# Else Clause
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally Clause
try:
    print("Hey!")
except:
    print("Something went wrong")
finally:
    print("The 'try except' block is finished")

# Nested Try-Except Example
try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except Exception as e:
        print(f"Error writing to the file: {e}")
    finally:
        f.close()
except Exception as e:
    print(f"Error opening the file: {e}")

# Python User Input
"""
- Use `input()` for user input in Python 3.
- Note: Wrap input processing in `try` blocks to handle unexpected input.
"""
# Uncomment the code below to test user input.
# username = input("Enter username: ")
# print("Username is:", username)

# Python String Formatting
"""
- Use `format()` or f-strings for formatting strings.
- f-strings (introduced in Python 3.6) are concise and readable.
"""

# Using format()
age = 20
txt = "My name is Keyur, I am {}"
print(txt.format(age))

# Using f-Strings
name = "Keyur"
txt = f"Python Tutorial by {name}"
print(txt)

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} INR"
print(txt)

# Multiple Values
quantity, itemno, price = 3, 567, 49
myorder = "I want {} pieces of item number {} for {:.2f} INR."
print(myorder.format(quantity, itemno, price))

# Using Index Numbers
myorder = "I want {0} pieces of item number {1} for {2:.2f} INR."
print(myorder.format(quantity, itemno, price))

# Named Indexes
myorder = "I want {quantity} pieces of item number {itemno} for {price:.2f} INR."
print(myorder.format(quantity=quantity, itemno=itemno, price=price))

########################### Exercise ###########################################

# Create a simple calculator program for arithmetic operations.


# Next Topic: File Handling --> Day 11
