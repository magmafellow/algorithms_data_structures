import math


# improvement over binary search best used for "uniformly" distributed data
#             "guesses" where a value might be based on calculated probe results
#             if probe is incorrect, search area is narrowed, and a new probe is calculated

#             average case: O(log(log(n)))
#             worst case: O(n) [values increase exponentially]



def interpolation_search(array, value):
    high = len(array) - 1
    low = 0

    while value >= array[low] and value <= array[high] and low <= high:

        probe = math.floor(low + (high - low) * (value - array[low]) / (array[high] - array[low]))

        print(f'probe: {probe}')

        if array[probe] == value:
            return probe
        elif array[probe] < value:
            low = probe + 1
        elif array[probe] > value:
            high = probe - 1

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 50, 59, 60, 199]

index = interpolation_search(array, 14)

if index > -1:
    print(index)
else:
    print('value was not found')
