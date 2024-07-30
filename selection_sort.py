



# selection sort = search through an array and keep the track of the minimum value during
#                  each iteration. At the end of each iteration, we swap variables.

#                  Quadratic time O(n^2)
#                  small data set = okay
#                  large data set = BAD



def selection_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]: min = j
        
        temp = a[i]
        a[i] = a[min]
        a[min] = temp




l = [9, 8, 5, 6, 2, 3, 1, 7, 4]

print('before selection sort')
print(l)
selection_sort(l)
print('after selection sort')
print(l)

