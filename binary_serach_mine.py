import math


def binary_search_mine(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = math.floor((high + low) / 2)
        expected_value = array[middle]

        if (expected_value == target): return middle
        elif (target > expected_value): low = middle + 1
        elif (target < expected_value): high = middle - 1
        else:
            print('Something went wrong')

    print(f'target[{target}] is not present in the given array')
    return -1


l = []

for i in range(15):
    l.append(i)

print(binary_search_mine(l, 10))
print(binary_search_mine(l, 35))
print(binary_search_mine(l, 2))

