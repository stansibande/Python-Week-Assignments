#name and age printing function
def nameAge(x,y):
    print ("My name is {} and i am {} Years old.".format(x,y))

#take two numbers and multiply them
def multiply(x,y):
    result=x*y
    print("{} X {} = {}.".format(x,y,result))


#take two numbers and check if a number x is a multiple of a number Y
def multiples(x,y):
    if x%y==0:
        print("The number {} is a multiple of the number {}".format(x,y))
        print
    else:
        print("The number {} is not a multiple of the number {}.".format(x,y))
        print()

#out of three numbers determine biggest and smallest
def checker(num1,num2,num3):
    if num1>num2:
        largest=num1
    else:
        largest=num2
    if num2>num3:
        largest=num2
    else:
        largest=num3
    if num3>largest:
        largest=num3
    else:
        largest=largest
    if largest>num1:
        largest=largest
    else:
        largest=num1
        
    print("The largest number between {},{} and {} is {}.".format(num1,num2,num3,largest))
    print()

#Example 1
print ("Enter Your Name and Age To Be Printed:")
name=input("Enter Your Full Name:")
try:
    age =int (input("Enter Your Age :"))
except:
    print ("Age can only be a number")
else:
    nameAge(name,age)
    print()
    
#Example 2
print ("Enter 2 numbers to be Submitted to a fuction for Multiplication:")
num1=int(input("Enter your First number: "))
num2=int (input("Enter your second Number: "))

multiply(num1,num2)
print()

#Example 3
print ("Enter 2 numbers to be Submitted to a fuction To Determine if the First number is a Multiple of the Second Number:")
mult1=int(input("Enter your First number: "))
mult2=int (input("Enter your second Number: "))
multiples(mult1,mult2)

#Example 4
print ("Enter 3 numbers to be Submitted to a fuction To Determine Which one is the largest:")
n1=int(input("Enter your First number: "))
n2=int (input("Enter your second Number: "))
n3=int (input("Enter your third Number: "))
checker(n1,n2,n3)




