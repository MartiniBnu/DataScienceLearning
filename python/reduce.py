from functools import reduce

def sum(x,y):
    return x + y

list = [1,2,3,4,54,121]

summed = reduce(sum, list)
print(summed)