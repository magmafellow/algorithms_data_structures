import time 



from linked_list import LinkedList


ll = LinkedList()
l = []

for i in range(20_000):
    ll.insertAtEnd(i)
    l.append(i)



ll_start = time.time()

ll.remove_node(100)
ll.remove_node(15000)
ll.remove_node(8000)

for i in range(4000):
    ll.insertAtIndex(10, i)

ll_end = time.time()
ll_elapsed = ll_end - ll_start
print('Linked list result:\t{}'.format(ll_elapsed))


l_start = time.time()

l.remove(100)
l.remove(15000)
l.remove(8000)

for i in range(4000):
    l.insert(i, 10)

l_end = time.time()
l_elapsed = l_end - l_start
print('ArrayList(list) result:\t{}'.format(l_elapsed))


