## Take in a row number from 1 to 5 inclusive and a column number from 1 to 5. Print out a grid of 0s, but in the row and column entered by the user, print a 1.

x = True
while x == True:
    try:
        r = int(input("Enter a row num from 1 to 5: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    if (1 <= r <= 5):
        x = False
    else:
        print("invalid input; please try again")

y = True
while y == True:
    try:
        c = int(input("Enter a col num from 1 to 5: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    if (1 <= c <= 5):
        y = False
    else:
        print("invalid input; please try again")

zeroRows = list((0,0,0,0,0))
nonZeroRows = zeroRows.copy()
nonZeroRows[c-1] = 1
for z in range(5):
    if z == (r-1):
        for i in nonZeroRows:
            print(i, " ", end = " ")
    else:
        for i in zeroRows:
            print(i, " ", end = " ")
    print()




