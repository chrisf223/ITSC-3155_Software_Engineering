##Write a script that takes in a string from the user. Print the string where all the lower case letters are shifted to the front and the spaces removed. 
##Keep the relative order of the lower case letters and upper case letters.

inp = input("Enter a String: ")
inpSize = len(inp)
lowString =""
upString = ""
letterIndex = len(inp)-1
for x in range(inpSize):
    stringToChar = inp[x]
    if stringToChar.islower():
        lowString += inp[x]
for x in range(inpSize):
    stringToChar = inp[x]
    if stringToChar.isupper():
        upString += inp[x]
newString =  lowString + upString
newString.replace(" ","")
print(newString)