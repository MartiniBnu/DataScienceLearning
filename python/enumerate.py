### simple solution
list = ["avocate","dog","ball"]
for i in list:
    print(i)

### with range
for i in range(len(list)):    
    print(i, list[i])


### with enumerate
for i, name in enumerate(list):
    print(i, name)    