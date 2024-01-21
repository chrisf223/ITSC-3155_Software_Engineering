## Write a script that takes in a string from the user. Print the string out backwards.

inp = input("Enter a String: ")
backwards = ""
inpSize = len(inp)
letterIndex = len(inp)-1
backwardsString = ""
for x in range(inpSize):
    backwardsString = backwardsString + inp[letterIndex]
    letterIndex -= 1
print(backwardsString)