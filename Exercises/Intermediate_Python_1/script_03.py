## Take in a string from the user and pass it as input to a function. 
## Have the function return a dict which keeps count of each letter (in lowercase) in the string, excluding spaces. Print out this dict.

def get_number_of_letters(string):
    string = string.lower()
    string = string.replace(" ","")
    searchedList = list()
    letterCount = 0 
    letterDict = dict()
    for x in range(len(string)):
        for y in range(len(string)):
            if string[x] == string[y] and not x in searchedList:
                letterCount += 1
        letterDict.update({string[x]:letterCount})
        searchedList.append(x)
        letterCount = 0
    return letterDict


inp = input("enter a String: ")
print(get_number_of_letters(inp))

