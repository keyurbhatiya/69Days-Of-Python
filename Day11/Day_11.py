################################## Day 11: 69 Days of Python #####################################


# File Handling

# Python File Open
# The open() function is used to open a file. It returns a file object, which has
# various methods and attributes that can be used to perform operations on the file
# The mode parameter is used to specify the mode in which the file is to be opened.
# The most commonly used modes are 'r' for reading, 'w' for writing, and 'a' for appending.
# If the mode is not specified, the file is opened in read mode by default.
# The 'r+' mode is used to open the file in both read and write mode

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

# syntax
# open(filename, mode)
f = open("demofile.txt")

# open a file for reading
f = open("demofile.txt", "rt")


# Exmple
f = open("demofile.txt", "r")
print(f.read())

# Open a file on a different location
f = open("C:\\Users\\keyur\\Desktop\\Python_complete_69Days\\69Days-Of-Python\\Day11\\demofile.txt", "r")
print(f.read())

# reak only
f = open("demofile.txt", "r")
print(f.readline())

# Read Lines
f = open("demofile.txt", "r")
print(f.readlines())


# Close Files
f = open("demofile.txt", "r")
print(f.readline())
f.close()




# Write to an Existing File

'''To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content'''

f = open("demofile.txt", "a")
# f.write(" Now the file has more content!")
f.close()

x = open("demofile.txt", "r")
print(x.read())


# Create a New File
# The "x" mode will create a new file for writing, and will throw an error if
# the file already exists.
# f = open("demofile.txt", "x") # error because the file already exists
# f = open("demo.txt", "x") # This will create a new file
# f.write("Now the file has more content!")
# f.close

'''"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists'''


# Delete a File
# The os.remove() function deletes a file. The file path is passed as an argument to the
# function.
import os
# os.remove("demofile.txt") # deletes the file


# Check if File exist:
import os
# Check if file exists
if os.path.exists("demofile.txt"):
    print("The file exists")
else:
    print("The file does not exist")

# Delete Folder
# The os.rmdir() function deletes a folder. The folder path is passed as an argument to
# the function.
import os
# os.rmdir("myfolder")


# Next Topic Python Modules NumPy ---> Day_12