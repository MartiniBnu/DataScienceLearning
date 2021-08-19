number1 = 0
number2 = 0
try:
    number1 = int(input("Number 1:"))
except:
    print("Invalid input!")  

try:
    number2 = int(input("Number 2:"))
except:
    print("Invalid input!")    

try:
    signal = input("Chose your signal [+,-,*,/]:")
except:
    print("Invalid input!")        

if signal == "+":
    print("Sum = "+str(number1+number2))
elif signal == "-":
    print("Minus = "+str(number1-number2))
elif signal == "*":
    print("Plus = "+str(number1*number2))
elif signal == "/":
    print("Division = "+str(number1/number2))
else:
    print("Invalid signal")

