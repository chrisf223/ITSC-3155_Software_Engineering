## Take in an integer greater than 1. Print out the cubes of each integer from 0 to the inputted integer.

x = True 

while x == True:
    try:
        integer = int(input("Enter an integer greater than 1: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    if integer >= 2:
        x = False
    else: 
        print("invalid input; please try again")

cubedInteger = integer * integer * integer

print("The cube of " + str(integer) + " is " + str(cubedInteger))
