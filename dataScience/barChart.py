## Data View on Python
import matplotlib.pyplot as plt

x = [1,2,3,4,5,78]
y = [2,3,7,1,3,11]
title = "Bar Chart"
xAxis = "X Axis"
yAxis = "Y Axis"


# Title
plt.title(title)
#Axes
plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.bar(x, y)
plt.savefig("dataScience/barChart.png")
