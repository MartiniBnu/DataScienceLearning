age = 0
adultAge = 18
try:
    age = int(input("How old are you? [Number]:"))
    if age < adultAge:
        print("Ok, you're a child yet! Have fun!!!")
    else:
        print("Caution!!! You might be arrested if you make some bullshit!")
except:
    print("Invalid input!")    