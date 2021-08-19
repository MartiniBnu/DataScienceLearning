a = "Marcos"
b = "Martini"

print(a,b)

concatenar = a + b + "\n"
print(concatenar)
print(len(concatenar))


print(concatenar[3])

#from 2 to 5
print(concatenar[2:5])
#Every String is a Object


print(concatenar.lower())
print(concatenar.upper())

# Spaces and special chars remove
print((concatenar+"   \n").strip())


outraString = "O rato roeu a roupa do rei de Roma"
splitString = outraString.split(" ")
print(splitString)

for i in splitString:
    print(i)


searchString = outraString.find("rei")
print(outraString[searchString:])

outraString = outraString.replace("rei","rainha")
print(outraString)
