## Take in 10 integers from user. Create a new list with only elements which appear once. Print both lists.

num = 1
range = 10
intList = list()
while range > 0:
    try:
        inp = int(input("Enter number " + str(num) + ": "))
    except ValueError:
            print("invalid input; please try again")
            continue
    num = num + 1
    range = range - 1
    intList.append(inp)
print("Original List: " + str(intList))

copyList = intList.copy()
onceList = intList.copy()
for x in intList:
     for y in copyList:
          if x == y:
               onceList.remove(y)
print("Nums that appear once: " + str(onceList))
