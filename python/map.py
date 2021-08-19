def double(x):
    return x*2

value = 2
print(double(value))    

#### If we pass a list, python will just duplicate the list
list = [1,2,3,4,5]
print(double(list))

### We can map the list to double all the list members

mapped_list = map(double, list)

for v in mapped_list:
    print(v)