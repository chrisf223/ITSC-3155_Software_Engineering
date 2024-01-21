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