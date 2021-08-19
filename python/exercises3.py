import math


#delta 
def delta (a, b, c):
    return b * b -4 * a * c

#square root commom
def squareCommom(a,b,c):
    return (math.sqrt(delta(a, b, c)))

#square root 1
def square1(a, b, c):
    return (-b + squareCommom(a,b,c) ) / 2 * a

#square root 2
def square2(a, b, c):
    return (-b + squareCommom(a,b,c) ) / 2 * a

a = 1
b = 0 
c = -16

print("Delta = " + str(delta(a, b, c)))
print("Square Root 1 = " + str(square1(a, b, c)))
print("Square Root 2 = " + str(square2(a, b, c)))


