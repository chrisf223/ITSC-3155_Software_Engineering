## Write a script that takes in a grade from 0-100 inclusive. Assuming a normal 10 point grading scale, print off whether the user got an A, B, C, D, or F.

x = True

while x == True:
    try:
        grade = float(input("Enter a grade from 0-100: "))
    except ValueError:
        print("invalid input; please try again")
        continue
    if 0.0 <= grade <=100.0:
        x = False
    else: 
        print("invalid input; please try again")

if grade < 60.0:
    print("Your grade is an F")
elif grade < 69.5:
    print("Your grade is an D")
elif grade < 79.5:
    print("Your grade is an C")
elif grade < 89.5:
    print("Your grade is an B")
else:
    print("Your grade is an A")