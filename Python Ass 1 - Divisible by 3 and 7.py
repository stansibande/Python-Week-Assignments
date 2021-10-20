#Assignments
#1 program to check whether a number is divisible by both 3 and 7, display appropriate message of choice

print ("This program will Accept A Number From you and Determine if the number is Divisible By Both 3 And 7")
print ("-------------------")

userNum=1

while userNum%3!=0 and userNum%7!=0:
    userNum=int (input ("Enter Any Number:"))

    if userNum%3==0 and userNum%7==0:
        print ("----------------------------------------------------------------")
        print()
        print("The Number you Entered,",userNum," is Divisible By Both 3 and 7")
        print("Congraturations!!! The Program will now Exit.")
        print ("----------------------------------------------------------------")

    else:
        print ("----------------------------------------------------------------")
        print()
        print("The Number you Entered (",userNum,"), is Not Divisible By Both 3 and 7")
        print("Please Try Again")
        print ("----------------------------------------------------------------")
    
