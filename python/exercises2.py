mininumGrade = 6
gradeList = [-1,-1]

i = 0
while i < 2:
    validGrade = False
    while not validGrade:
        try:
            gradeList[i] = int(input("What was your grade #"+str(i+1)+"? [0-10]:"))
            if gradeList[i] < 0 or gradeList[i]  > 10:
                print("Invalid grade #"+str(i+1)+" input! You've to input some numeric number from 0 to 10!")
            else:
                validGrade = True
        except:
            print("Invalid grade #"+str(i+1)+" input!")    
    i += 1

avg = (gradeList[0] + gradeList[1]) / 2
print("Your average grade is: " + str(avg))
if avg >= mininumGrade:
    print("You've passed in the semester!")
else:
    print("You're fucked man!!! We'll see you again on the next semester!")