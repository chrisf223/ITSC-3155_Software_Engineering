## Take in 5 words from the user and store them in a list. Then, create a single string from the individual words, separated by spaces, and print the list and resultant string.

wordList = list()
for x in range(5):
    inp = input("Enter a word: ")
    wordList.append(inp)
sentence = ""
for x in wordList:
    sentence = sentence + x + " " 
print("Words: " + str(wordList))
print("One String: " + sentence)
