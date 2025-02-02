import matplotlib.pyplot as plt
import numpy as np

# 1. Matplotlib Intro
print("Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.")

# 2. Matplotlib Get Started
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.plot(x, y)
plt.title("Matplotlib Get Started")
plt.show()

# 3. Matplotlib Pyplot
print("Pyplot provides a MATLAB-like interface to Matplotlib.")
plt.plot(x, y)
plt.title("Matplotlib Pyplot Example")
plt.show()

# 4. Matplotlib Plotting
plt.plot(x, y, marker='o')
plt.title("Matplotlib Plotting Example")
plt.show()

# 5. Matplotlib Markers
plt.plot(x, y, marker='*', linestyle='--', color='r')
plt.title("Matplotlib Markers Example")
plt.show()

# 6. Matplotlib Line
plt.plot(x, y, linestyle=':')
plt.title("Matplotlib Line Styles Example")
plt.show()

# 7. Matplotlib Labels
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Matplotlib Labels Example")
plt.show()

# 8. Matplotlib Grid
plt.plot(x, y)
plt.grid()
plt.title("Matplotlib Grid Example")
plt.show()

# 9. Matplotlib Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("First Subplot")

plt.subplot(1, 2, 2)
plt.plot(y, x)
plt.title("Second Subplot")

plt.suptitle("Matplotlib Subplot Example")
plt.show()

# 10. Matplotlib Scatter
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11])
y = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78])
plt.scatter(x, y)
plt.title("Matplotlib Scatter Example")
plt.show()

# 11. Matplotlib Bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y)
plt.title("Matplotlib Bars Example")
plt.show()

# 12. Matplotlib Histograms
data = np.random.normal(170, 10, 250)
plt.hist(data)
plt.title("Matplotlib Histogram Example")
plt.show()

# 13. Matplotlib Pie Charts
sizes = [15, 30, 45, 10]
labels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Matplotlib Pie Chart Example")
plt.show()


''' Next Topic Machine Learning ---> Day_24.py '''
