## Data View on Python
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]
z = [20, 400, 100, 33, 10]

title = "ScatterPlot Chart"
xAxis = "X Axis"
yAxis = "Y Axis"


# Title
plt.title(title)
#Axes
plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.scatter(x, y, label="MyDots", color="k", marker=".", s=z)
plt.plot(x,y, color="#990000", linestyle="--")
plt.legend()

plt.savefig("dataScience/scatterPlot.png",dpi=1200)

### docs
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
