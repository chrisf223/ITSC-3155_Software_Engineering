## Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store them in a separate list. 
## Create a third array containing the common values from both arrays without duplicates. Print out all three lists.

x = 5
listOne = list()
while x > 0:
    try:
        n = int(input("Enter a number for the first list: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    listOne.append(n)
    x = x-1
x = 5
listTwo = list()
while x > 0:
    try:
        n = int(input("Enter a number for the second list: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    listTwo.append(n)
    x = x-1

listCommon = list()
for y in listOne: 
    for z in listTwo:
        if y == z:
            listCommon.append(y)

print("First List: " + str(listOne))
print("Second List: " + str(listTwo))
print("Common List: " + str(listCommon))