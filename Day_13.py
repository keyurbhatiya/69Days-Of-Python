################################## Day 13: 69 Days of Python #####################################

# What is a Random Number?
# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

#example of random number int
import random
random_number = random.randint(1, 10) # returns a random number between 1 and 10
print(random_number)

#example of random number float
random_number = random.uniform(1.0, 10.0) # returns a random number between 1.0 and 10.0
print(random_number)

# Generate Random Array

import numpy as np

random_array = np.random.randint(1, 10, size=(3, 3))
print(random_array)

# Shuffling Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)

print(arr)

# Generating Permutation of Arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.random.permutation(arr))



# Seaborn

# Plotting a Distplot
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a Distplot Without the Histogram
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

# normal distribution
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

# Binomial Distribution
# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

# Difference Between Normal and Binomial Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()

# Poisson 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()


####################################### numpy_ufunc_tutorial #########################3

import numpy as np


# 1. ufunc Introduction

# ufunc stands for "universal functions" in NumPy.
# They are vectorized wrappers for performing element-wise operations on arrays.

# Example: Add two arrays element-wise
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.add(arr1, arr2)
print("1. ufunc Add Example:", result)

# 2. ufunc Create Function

# You can create your own ufunc using NumPy's `frompyfunc`.

def multiply_elements(x, y):
    return x * y

multiply_ufunc = np.frompyfunc(multiply_elements, 2, 1)  # 2 inputs, 1 output
result = multiply_ufunc([1, 2, 3], [4, 5, 6])
print("2. Custom ufunc Multiply Example:", result)


# 3. ufunc Simple Arithmetic

# Arithmetic operations with ufuncs
arr = np.array([10, 20, 30])
print("3. Add 5 to Array:", np.add(arr, 5))  # Add 5 to each element
print("3. Subtract 5 from Array:", np.subtract(arr, 5))  # Subtract 5
print("3. Multiply Array by 2:", np.multiply(arr, 2))  # Multiply by 2
print("3. Divide Array by 10:", np.divide(arr, 10))  # Divide by 10


# 4. ufunc Rounding Decimals

# Round numbers to the nearest integer or specified decimals
arr = np.array([1.123, 2.678, 3.456])
print("4. Round to Nearest Integer:", np.around(arr))
print("4. Round to 1 Decimal Place:", np.around(arr, decimals=1))


# 5. ufunc Logs

# Compute the natural log, base-10 log, and base-2 log
arr = np.array([1, 10, 100])
print("5. Natural Log:", np.log(arr))  # ln(x)
print("5. Base-10 Log:", np.log10(arr))  # log10(x)
print("5. Base-2 Log:", np.log2(arr))  # log2(x)

# 6. ufunc Summations

# Compute the sum of array elements
arr = np.array([1, 2, 3, 4, 5])
print("6. Sum of Array:", np.sum(arr))
print("6. Cumulative Sum:", np.cumsum(arr))  # Cumulative sum


# 7. ufunc Products

# Compute the product of array elements
print("7. Product of Array:", np.prod(arr))
print("7. Cumulative Product:", np.cumprod(arr))  # Cumulative product


# 8. ufunc Differences

# Compute the difference between consecutive elements
print("8. Differences in Array:", np.diff(arr))


# 9. ufunc Finding LCM (Least Common Multiple)

# Find the least common multiple of array elements
arr = np.array([4, 6, 8])
print("9. LCM of Array:", np.lcm.reduce(arr))

# 10. ufunc Finding GCD (Greatest Common Divisor)

# Find the greatest common divisor of array elements
arr = np.array([8, 16, 32])
print("10. GCD of Array:", np.gcd.reduce(arr))


# 11. ufunc Trigonometric

# Perform trigonometric operations
angles = np.array([0, np.pi/2, np.pi])
print("11. Sine of Angles:", np.sin(angles))
print("11. Cosine of Angles:", np.cos(angles))
print("11. Tangent of Angles:", np.tan(angles))


# 12. ufunc Hyperbolic

# Perform hyperbolic operations
values = np.array([0, 1, 2])
print("12. Hyperbolic Sine:", np.sinh(values))
print("12. Hyperbolic Cosine:", np.cosh(values))
print("12. Hyperbolic Tangent:", np.tanh(values))


# 13. ufunc Set Operations

# Perform set operations with NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
print("13. Union of Arrays:", np.union1d(arr1, arr2))
print("13. Intersection of Arrays:", np.intersect1d(arr1, arr2))
print("13. Difference of Arrays:", np.setdiff1d(arr1, arr2))
print("13. Symmetric Difference:", np.setxor1d(arr1, arr2))


''' Next Topic: Pandas Tutorial ---> Day_14 '''