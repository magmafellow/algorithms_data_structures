import math





# mergeSort

def populate_array(size):
    l = []
    for i in range(size):
        l.append('<blank>')

    return l


def merge(left_array, right_array, array):
    left_size = math.floor(len(array) / 2)
    right_size = len(array) - left_size

    i = 0
    l = 0
    r = 0

    # check conditions for merging
    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            i += 1
            r += 1
        
    while l < left_size:
        array[i] = left_array[l]
        i += 1
        l += 1

    while r < right_size:
        array[i] = right_array[r]
        i += 1
        r += 1
    


def merge_sort(array):
    length = len(array)
    if length <= 1: return

    middle = math.floor(length / 2)
    left_array = populate_array(middle)
    right_array = populate_array(length - middle)

    # i = 0  # left array
    j = 0  # right array

    for i in range(length):
        if (i < middle):
            left_array[i] = array[i]
        else:
            right_array[j] = array[i]
            j += 1

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)


l = [8, 2, 3, 6, 5, 1, 9, 8, 7]

print(l)
merge_sort(l)
print('after sort')
print(l)

