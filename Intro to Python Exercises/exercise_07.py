## Take in integers until the user types "QUIT" and store the numbers in a list. 
## Assume any input other than "QUIT" is a valid integer. Create another list of just the even numbers and print both lists.

hasQuit = False
originalList = list()
while hasQuit == False:
    inp = input("Enter a number or QUIT to quit: ")
    if inp == "QUIT":
        break
    else:
        try: 
            originalList.append(int(inp))
        except ValueError:
            print("invalid input; please try again")
            continue
print("OrignalList: " + str(originalList))

evenList = list()
for x in originalList:
    if (x % 2 == 0):
        evenList.append(x)
print("Even Nums: " + str(evenList))
