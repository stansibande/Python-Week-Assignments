#Assignment
print("----------------------------------------------------------------------------------------")
print()
print ("This program will accept price of a bike and print out road Tax depending on the price")
print()
print("----------------------------------------------------------------------------------------")

taxRate1=15
taxRate2=10
taxRate3=5

bikePrice=float(input("Please Enter the Price Of The Bike in Rs :"))

if bikePrice>100000:
    tax=(bikePrice/100)*taxRate1
    print("----------------------------------------------------------------------------------------")
    print()
    print("The Road Tax Rate for The Bike you Just Purchased at Rs",bikePrice, " , is",taxRate1,"%. You Will Pay Rs",tax,". Thank You")
    print()
    print("----------------------------------------------------------------------------------------")
    
elif bikePrice>50000 and bikePrice<=100000:
    tax=(bikePrice/100)*taxRate2
    print("----------------------------------------------------------------------------------------")
    print()
    print("The Road Tax Rate for The Bike you Just Purchased at Rs",bikePrice, " , is",taxRate2,"%. You Will Pay Rs",tax,". Thank You")
    print()
    print("----------------------------------------------------------------------------------------")
    
elif bikePrice<=50000:
    tax=(bikePrice/100)*taxRate3
    print("----------------------------------------------------------------------------------------")
    print()
    print("The Road Tax Rate for The Bike you Just Purchased at Rs",bikePrice, " , is",taxRate3,"%. You Will Pay Rs",tax,". Thank You")
    print()
    print("----------------------------------------------------------------------------------------")
