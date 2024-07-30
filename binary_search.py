import math


def binary_search(array, target):
    
    low = 0
    high = len(array) - 1
    
    while (low <= high):

        middle = math.floor(low + (high - low) / 2)
        value = array[middle]
        
        print(value)
        
        if value < target:
            low = middle + 1
        elif value > target:
            high = middle - 1
        else:
            return middle  # target found

    return -1  # target not found


l = []

for i in range(100):
    l.append(i)


print(binary_search(l, 77))

