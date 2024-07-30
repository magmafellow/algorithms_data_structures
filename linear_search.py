# linear search = Iterate through a collection one element at a time

# runtime complexity: O(n)

# Disadvantages:
#   -> Slow for large data sets

# Advantages:
#   -> Fast for searches of small to medium data sets
#   -> Does not need to be sorted (Huge advantage!!!)
#   -> Useful for data structures that do not have random access (Linked List)

def linearSearch(array, value):

    i = 0
    while (i < len(array)):
        if array[i] == value:
            return i
        i = i+1

    return -1

array = [9, 8, 3, 2, 5, 7, 6, 1]

index = linearSearch(array, 3)

if index != -1:
    print('We found this! At index {}'.format(index))
else:
    print('Element not found')

