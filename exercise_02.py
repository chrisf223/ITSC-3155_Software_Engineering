## Write a script that takes in two strings from the user. If one string is the suffix of the other string, print "True", otherwise, print "False".

stringOne = input("Enter a string: ")
stringTwo = input("Enter another string: ")
stringOneLength = len(stringOne)
stringTwoLength = len(stringTwo)

if stringOneLength ==  stringTwoLength:
    if stringOne == stringTwo:
        print("True") 
    else:
        print("False")
elif stringOneLength > stringTwoLength:
    stringOneSuffix = stringOne[(stringOneLength-stringTwoLength):]
    if stringOneSuffix == stringTwo:
        print("True")
    else:
        print("False")
else:
    stringTwoSuffix = stringTwo[(stringTwoLength-stringOneLength):]
    if stringTwoSuffix == stringOne:
        print("True")
    else:
        print("False")