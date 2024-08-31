## Write an implementation of the fibonacci sequence that computes the nth term of the sequence where n is a random number from 15 to 35 inclusive. 
## Time the number of seconds your implementation takes with the Python time moduleLinks to an external site. 
## Print out both the result of your script's fibonacci function and the time it took
import random
import time

startTime = time.time()
sequence_number = (random.randint(15,35))
x_minus_two = 0
x_minus_one = 1
next_number = x_minus_one 
count = 1

while count <= (sequence_number-2):
	count += 1
	x_minus_two, x_minus_one = x_minus_one, next_number
	next_number = x_minus_two + x_minus_one

print("fib(" + str(sequence_number) + ") = " + str(next_number))
endTime = time.time()
totatlTime = endTime - startTime
print("fib(" + str(sequence_number) + ") took " + str(totatlTime) + " seconds")