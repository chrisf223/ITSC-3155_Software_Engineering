## Write a function that takes in a list data structure as input. The function should create a new list and only include unique elements of the inputted list. 
## Under the function, write code that calls the function with a test list and print out the result.

def get_unique_list(my_list):
    uniqueList = list()
    for x in my_list:

        if x not in (uniqueList):
            uniqueList.append(x)
    return uniqueList


my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print("Unique List: " + str(unique_list))