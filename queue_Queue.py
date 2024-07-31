# Queue = FIFO data structure. First-In First-Out (ex. A line of people)
#           A collection designed for holding elements prior to processing
#           Linear data structure

#           add       = enqueue, offer()
#           remove    = dequeue, poll()


from queue import Queue


q = Queue(maxsize=15)

print('Size of q at the start point {}'.format(q.qsize()))

q.put('a')
q.put('b')
q.put('c')

print(q.get())
print(q.get())
print(q.get())

print(f'Empty: {q.empty()}')

q.put(1)
print('one has been added')
print(f'Empty: {q.empty()}')


