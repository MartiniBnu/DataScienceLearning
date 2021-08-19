list1 = [1,2,3,4,5]
list2 = ["ball","dog","subway","tree","lower"]

for number, name in zip(list1, list2):
    print(number, name)

list3 = ["R$2,00","R$0,00","R$250,00","R$5,00","R$0,00"]    

for number, name, value in zip(list1, list2, list3):
    print(number, name, value)
