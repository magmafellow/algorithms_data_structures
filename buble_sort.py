



# buble sort = pairs of adjacent elements are compared, and the elements
#              swapped if they are not in order

#              Quadratic time O(n^2)
#              small data set = okay-ish
#              large data set = BAD (plz don't)


l = [9, 8, 5, 4, 6, 3, 7, 1, 2]

def buble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

buble_sort(l)
print('after buble sort')
print(l)
