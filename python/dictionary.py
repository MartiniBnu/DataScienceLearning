siteDictionary = {"Martini": "martini.bnu@gmail.com"
                   ,"Simoni": "simonibnu@gmail.com"}
print(siteDictionary['Martini'])
print(len(siteDictionary))

for key in siteDictionary:
    print(siteDictionary[key])

#Tupla
for item in siteDictionary.items():
    print(item)    

#Keys
for key in siteDictionary.keys():
    print(key)    

#Values    
for value in siteDictionary.values():
    print(value)    
