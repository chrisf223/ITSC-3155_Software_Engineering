## Take in a string from the user and split it into an array of single characters. Split the list of characters into a list of lists where each inner list has 3 elements.
## Notice that the last inner array may have less than 3 elements.

inp = input("Enter a String: ")
characterList = list()
for x in range(len(inp)):
    characterList.append(inp[x])

threeElementsList = list()
finalList = list()
y = True
while y == True: 
    for x in range(3):
        if len(characterList) > 0:
            threeElementsList.append(characterList[0])
            characterList.pop(0)
        else:
            y = False
    finalList.append(threeElementsList.copy())
    threeElementsList.clear()

print(finalList)
