## Take in 5 int inputs from the user and add them together. The catch is that you can no longer assume that what the user enters is a valid int. 
## If the user enters an invalid input, print an error message and make the user input the int again until all 5 int values are entered correctly. 
## Print the resulting sum.

num = 1
range = 5
intList = list()
while range > 0:
    try:
        inp = int(input("Enter number " + str(num) + ": "))
    except ValueError:
            print("invalid input; please try again")
            continue
    num = num + 1
    range = range - 1
    intList.append(inp)
sum = 0
for x in intList:
     sum = sum + x
print("Your Sum Is: " + str(sum))