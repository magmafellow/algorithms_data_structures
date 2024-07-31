# stack = LIFO data structure. Last-In First-Out
#         stores objects into a short of "vertical tower"
#         push() to add to the top
#         pop() to remove from the top


# class MyStack:
  
#   def __init__(self, *args):
#     self.main = []
#     for i in args:
#       self.main.append(i)
    
#   def show(self):
#     for i in self.main:
#       print(i)



# my_stack = MyStack('a', 'b', 'c', 'd')

# my_stack.show()



### collections.deque

from collections import deque

stack = deque()

# append() = push()

stack.append('a')
stack.append('b')
stack.append('c')

print(f'Initial stack {stack}')

# pop()
print('Elements popped from stack')
print(stack.pop())
print(f'Stack in between of popping elements: {stack}')
print(stack.pop())
print(stack.pop())

print(f'Stack after elements are popped: {stack}')
