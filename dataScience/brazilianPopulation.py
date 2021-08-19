## Brazilian population growth from 1980 till 2021
## DataSUS
import matplotlib.pyplot as plt
data = open("dataScience/populacao_brasileira.csv").readlines()

xYear = []
yPopulation = []

for i in range(1,len(data)):
    lineData = data[i].split(";")  
    xYear.append(int(lineData[0]))
    yPopulation.append(int(lineData[1]))

plt.title("Braziliar Growth from "+str(xYear[0])+" to "+str(xYear[len(xYear)-1]))
plt.xlabel("Year")
plt.ylabel("Population*100mi")
plt.bar(xYear,yPopulation, color="skyblue")
plt.plot(xYear,yPopulation, color="black", linestyle="--")

plt.savefig("dataScience/BraziliarGrowth.png", dpi=300)