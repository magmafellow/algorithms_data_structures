


# insertion search = after comparing elements to the left
#                    shift elements to the right to make room to insert a value

#                    Quadratic time O(n^2)



def insertion_search(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1

        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1]=temp 




l = [9, 1, 8, 2, 7, 3, 5, 4, 6, 0]


for i in l:
    print(i, end=" ")
print()

insertion_search(l)

print(l)

