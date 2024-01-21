## Take in a number, n, from the user. Then, take in n floats from the user and store them in a list. Print the list and the mean.

x = True
while x == True:
    try:
        n = int(input("Enter an integer greater than 1: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    if n >= 2:
            x = False
    else: 
        print("invalid input; please try again")

floatList = list()
listNumber = 1
numberOfFloats = n
while n > 0:
    try:
        addFloat = float(input("Enter number " + str(listNumber) + ": "))
    except ValueError:
        print("invalid input; please try again")
        continue
    floatList.append(addFloat)
    n = n-1
    listNumber = listNumber + 1

print("List: " + str(floatList))
sum = 0
for x in floatList:
    sum = sum + x
average = sum/numberOfFloats
print("Average: " + str(average))