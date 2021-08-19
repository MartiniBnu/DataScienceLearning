import matplotlib.pyplot as plt
import random 


vetor = []
for i in range(10):
    randNumber = random.randint(0,10000)
    vetor.append(randNumber)

plt.boxplot(vetor)
plt.title("BoxPlot")
plt.savefig("dataScience/boxPlot.png", dpi=300)