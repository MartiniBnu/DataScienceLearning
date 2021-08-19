myCustomList = [0,0]
myCustomList[0] = 20
print(myCustomList)



myRandonList = ["pineaple",1,False,2,True,"WTF"]
print(myRandonList)

#iteration
for item in myRandonList:
    print(item)

#list size
tamanho = len(myRandonList)
print(tamanho)


#list adition
myRandonList.append("Olá, entrei agora???")
print(myRandonList)

#list remove by value
myRandonList.remove(2) 
print(myRandonList)

#list remove by position
del myRandonList[3:]
print(myRandonList)


#Order
myNumericList = [14,2232,33,4,1,3334436,71,-8,-12219]
print(myNumericList)
#Just the thirdh element
print(myNumericList[2])

myNumericList.sort() #This method will sort and update the list
print(myNumericList) 
print(sorted(myNumericList)) #Function that return de list

#List reverse
myNumericList = [14,2232,33,4,1,3334436,71,-8,-12219]
myNumericList.reverse()
print(myNumericList)

#Sort desc
myNumericList.sort(reverse=True)
print(myNumericList)




myList = ["banana","pineaple","apple","oracle","watermelon"]
print(myList)

myList.sort()
print(myList)







