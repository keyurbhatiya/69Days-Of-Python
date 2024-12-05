################################## Day 12: 69 Days of Python #####################################


#  Python Modules NumPy
# NumPy Tutorial

'''
NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python". 
'''


# Installation of NumPy
# You can install NumPy using pip, which is Python's package manager.
# You can install it by running the following command in your terminal:
# pip install numpy

# Checking NumPy Version
# You can check the version of NumPy by running the following command in your terminal:
# python -c "import numpy; print(numpy.__version__)"    
import numpy
print(numpy.__version__)



# Example
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)  # Output: [1 2 3 4 5]


# Create a NumPy ndarray Object
# You can create a NumPy ndarray object using the array() function.
# Example
import numpy as np

arr = np.array([11, 12, 13, 41, 51])

print(arr)

print(type(arr))


# Dimensions in Arrays
# 0-D Arrays
# A 0-D array is a scalar value
# Example
import numpy as np
arr = np.array(5)
print(arr)
print(arr.ndim)

# 1-D Arrays
# A 1-D array is an array that has only one dimension.
# Example
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)

# 2-D Arrays
# A 2-D array is an array that has two dimensions.  
# Example
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)

# 3-D arrays
# A 3-D array is an array that has three dimensions.
# Example
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr.ndim)


# Higher Dimensional Arrays
# A higher dimensional array is an array that has more than three dimensions.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)



# Accessing Array Elements
# You can access array elements by their index.
# Index starts at 0.
# You can also use negative index to access elements from the end of the array.
# Example
print(a[0])  # Output: 1
print(a[-1])  # Output: 5

# Access 2-D Arrays
# You can access 2-D arrays by their index.
# Index starts at 0.
# Example
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1]) # Output: 2

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4]) # Output: 10


# Numpy Array Slicing
# You can slice an array to get a part of it.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])# Output: [2 3 4]

# STEP
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) # Output: [2 4]

# Data Types in NumPy
# NumPy supports the following data types:
# i- integer
# u- unsigned integer
# b- boolean
# f- float   
# c- complex float
# m- timedelta
# M- datetime
# O- object
# S- string
# U- unicode string
# V- fixed chunk of memory for other type ( void )


# Checking the Data Type of an Array	
# You can check the data type of an array by using the type() function.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(type(arr)) # Output: <class 'numpy.ndarray'>

# Creating Arrays With a Defined Data Type
# You can create an array with a defined data type using the dtype parameter.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='f')

print(arr) # Output: [1. 2. 3. 4.]


# Converting Data Type on Existing Arrays
# You can convert the data type of an existing array using the astype() method.
# Example
import numpy as np
arr = np.array([1, 2, 3, 4])# Output: [1 2 3 4]
newarr = arr.astype('f')
print(newarr)
print(newarr.dtype)

# NumPy Array Copy vs View
# A copy of an array is a new array with the same data as the original array.
# A view of an array is a new array that points to the same data as the original array.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) # Output: [42  2  3  4  5]
print(x) # Output: [1 2 3 4 5]

# VIEW:
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr) # Output: [42  2  3  4  5]
print(x) # Output: [42  2  3  4  5]

# Shape of an Array
# You can get the shape of an array by using the shape attribute.
# Example
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) # Output: (2, 4)

# NumPy Array Reshaping
# You can reshape an array by using the reshape() method.
# Reshape From 1-D to 2-D
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = arr.reshape(2, 3)

print(newarr) # Output: [[1 2 3] [4 5 6]]

# Reshape From 1-D to 3-D
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = arr.reshape(2, 3, 1)

print(newarr) # Output: [[[1] [2] [3]] [[4] [5] [6]]]


# Iterating Arrays
# You can iterate over an array using a for loop.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4])

for x in arr:
    print(x)

# Iterating 2-D Arrays
# You can iterate over a 2-D array using a nested for loop.
# Example
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in arr:
    for y in x:
        print(y)

# Iterating 3-D Arrays
# You can iterate over a 3-D array using a nested for loop.
# Example
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()
# The nditer() function is used to iterate over an array in a way that is similar to
# iterating over a list. It is more flexible than the for loop and can be used to
# iterate over arrays of any dimension.
# Example
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)


# Iterating Array With Different Data Types
# You can iterate over an array with different data types using the nditer() function.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

for x in np.nditer(arr):
    print(x)


# Iterating With Different Step Size
# You can iterate over an array with a different step size using the nditer() function.
# Example
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

# Enumerated Iteration Using ndenumerate()
# The ndenumerate() function is used to iterate over an array and get the index of each element
# Example
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)


# Joining NumPy Arrays
# You can join two or more arrays using the concatenate() function.
# Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# stack()
# The stack() function is used to stack arrays in sequence vertically or horizontally.
# Example
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
arr = np.stack((arr1, arr2, arr3), axis=0)

print(arr)


# hstack()
# The hstack() function is used to stack arrays in sequence horizontally.
# Example
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
arr = np.hstack((arr1, arr2, arr3))

print(arr)

# vstack()
# The vstack() function is used to stack arrays in sequence vertically.
# Example
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
arr = np.vstack((arr1, arr2, arr3))

print(arr)


# dstack()
# The dstack() function is used to stack arrays in sequence depthwise.
# Example
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
arr = np.dstack((arr1, arr2, arr3))

print(arr)

# Splitting NumPy Arrays
# You can split a NumPy array into two or more arrays using the split() function.
# Example
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

newarr = np.array_split(arr, 3)

print(newarr)

# Searching Arrays
# You can search for a specific value in an array using the where() function.
# Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

x = np.where(arr == 5)

print(x)


# Sorting Arrays
# You can sort an array using the sort() function.
# Example
import numpy as np

arr = np.array([3, 2, 0, 1])

arr.sort()

print(arr)


# Filtering Arrays
# You can filter an array using the where() function.
# Example
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# Creating the Filter Array
# Example
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # prints: [False, False, True, True]
print(newarr) # prints: [43 44]




# Next Topic Random Numbers in NumPy ---> Day_13