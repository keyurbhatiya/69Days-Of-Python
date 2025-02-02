################################## Day 15: 69 Days of Python #####################################
# SciPy

#example
import numpy as np
from scipy import constants, sparse, io
from scipy.optimize import root
from scipy.spatial import Delaunay, ConvexHull
from scipy.sparse.csgraph import connected_components
from scipy.interpolate import interp1d
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
from math import cos

# SciPy Constants
print(f"Liter: {constants.liter}")
print(f"Pi: {constants.pi}")

# Metric Prefixes
metric_prefixes = [constants.yotta, constants.zetta, constants.exa, constants.peta, constants.tera]
print("Metric Prefixes:", metric_prefixes)

# Binary Prefixes
binary_prefixes = [constants.kibi, constants.mebi, constants.gibi, constants.tebi]
print("Binary Prefixes:", binary_prefixes)

# Mass Units
mass_units = [constants.gram, constants.metric_ton, constants.lb, constants.oz]
print("Mass Units:", mass_units)

# Angle Units
angle_units = [constants.degree, constants.arcmin, constants.arcsecond]
print("Angle Units:", angle_units)

# Time Units
time_units = [constants.minute, constants.hour, constants.day, constants.year]
print("Time Units:", time_units)

# Length Units
length_units = [constants.inch, constants.foot, constants.mile, constants.point]
print("Length Units:", length_units)

# Pressure Units
pressure_units = [constants.atm, constants.bar, constants.torr, constants.psi]
print("Pressure Units:", pressure_units)

# Optimization Example
def eqn(x): return x + cos(x)
root_result = root(eqn, 0)
print(f"Root of equation: {root_result.x}")

# Sparse Data Example
A = sparse.csr_matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
print("Sparse Matrix:\n", A)

# Connected Components
arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
newarr = sparse.csr_matrix(arr)
n_components, labels = connected_components(newarr)
print(f"Connected Components: {n_components}, Labels: {labels}")

# Delaunay Triangulation
points = np.array([[2, 4], [3, 4], [3, 0], [2, 2], [4, 1]])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.title("Delaunay Triangulation")
plt.show()

# Convex Hull
points = np.array([[2, 4], [3, 4], [3, 0], [2, 2], [4, 1], [1, 2], [5, 0], [3, 1]])
hull = ConvexHull(points)
plt.scatter(points[:, 0], points[:, 1])
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.title("Convex Hull")
plt.show()

# MATLAB Arrays Example
arr = np.arange(10)
io.savemat('arr.mat', {"vec": arr})
mydata = io.loadmat('arr.mat')
print("MATLAB Data Imported:", mydata)

# Interpolation Example
xs, ys = np.arange(10), 2 * np.arange(10) + 1
interp_func = interp1d(xs, ys)
new_values = interp_func(np.arange(2.1, 3, 0.1))
print("Interpolated Values:", new_values)

# Statistical Significance Test
v1, v2 = np.random.normal(size=100), np.random.normal(size=100)
t_test_result = ttest_ind(v1, v2)
print("T-Test Result:", t_test_result)

''' Next Topic Django Tutorial ---> Day_16 '''