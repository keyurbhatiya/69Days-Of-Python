################################## Day 24: 69 Days of Python #####################################
# Machine Learning
# Machine Learning: A Comprehensive Beginner's Tutorial

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Getting Started
# Machine Learning (ML) enables systems to learn and make predictions based on data.
# This guide introduces fundamental concepts with examples for hands-on learning.

# Mean, Median, Mode
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode.mode)

# Standard Deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Percentile
percentile_25 = np.percentile(data, 25)
percentile_75 = np.percentile(data, 75)
print("25th Percentile:", percentile_25)
print("75th Percentile:", percentile_75)

# Data Distribution
plt.hist(data, bins=5, color='blue', alpha=0.7)
plt.title("Data Distribution")
plt.show()

# Normal Data Distribution
mean, std = 0, 1
normal_data = np.random.normal(mean, std, 1000)
plt.hist(normal_data, bins=30, color='green', alpha=0.7)
plt.title("Normal Distribution")
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Linear Regression
x = x.reshape(-1, 1)  # Reshape for sklearn
y = y.reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

plt.scatter(x, y, label="Data")
plt.plot(x, model.predict(x), color='red', label="Regression Line")
plt.legend()
plt.show()

# Polynomial Regression
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

model.fit(x_poly, y)
plt.scatter(x, y, label="Data")
plt.plot(x, model.predict(x_poly), color='purple', label="Polynomial Fit")
plt.legend()
plt.show()

# Multiple Regression
x_multi = np.random.rand(100, 2)
y_multi = 3 * x_multi[:, 0] + 2 * x_multi[:, 1] + np.random.normal(0, 0.2, 100)

model.fit(x_multi, y_multi)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_multi)
print(x_scaled[:5])

# Train/Test Split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_multi, test_size=0.2, random_state=42)
model.fit(x_train, y_train)
print("Test Score:", model.score(x_test, y_test))

# Decision Tree
tree = DecisionTreeRegressor()
tree.fit(x_train, y_train)

# Predict and Visualize
predictions = tree.predict(x_test)
plt.scatter(y_test, predictions)
plt.title("Decision Tree Predictions")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()


# summary
# - linear regression: simple linear regression, multiple linear regression, polynomial regression
# - decision tree: classification, regression
# - machine learning: supervised learning, unsupervised learning

# reference
# - https://scikit-learn.org/stable/modules/classes.html


''' Next Topic Confusion Matrix ---> Day_25.py '''