## Data View on Python
import matplotlib.pyplot as plt

x = [1,2,5]
y = [2,3,7]

# Title
plt.title("My First Chart with Python")

#Axes
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.plot(x, y)
plt.savefig("dataScience/lineChart.png")
