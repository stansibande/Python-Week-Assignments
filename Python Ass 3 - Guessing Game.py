#assighnment

#for the rand function
import random
print("----------------------------------------------------------------------------------------")
print()
print("This Program will generate a number between 1 and 10 and ask you to guess, you can try guessing as many times as You Want")
print()
print("----------------------------------------------------------------------------------------")
print()
#generate random number between 1 and 10
randomNumber=random.randint(1,10)

userGuess=0
trys=0

while userGuess!=randomNumber:
    trys+=1
    
    print("----------------------------------------------------------------------------------------")
    print()
    userGuess=int(input("The System has Generated a Number Between 1 and 10, Enter your Guess!! :"))
    print()
    print("----------------------------------------------------------------------------------------")
    
    if userGuess==randomNumber:
        print("----------------------------------------------------------------------------------------")
        print()
        print("Congraturations!!, you Guessed correctly, And all it took you was",trys,"try(s)")
        print()
        print("----------------------------------------------------------------------------------------")
        
    else:
        print("----------------------------------------------------------------------------------------")
        print()
        print("Sorry, you guessed Wrong, Please Try Again")
        print()
        print("----------------------------------------------------------------------------------------")
              
              
