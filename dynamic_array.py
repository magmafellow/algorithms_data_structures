

class DynamicArray:
  def __init__(self, capacity=None):
    if capacity:
      self.capacity = capacity
    else:
      self.capacity = 5
    
    self.array = ['<empty_cell>' for i in range(self.capacity)]
    self.size = 0
  
  def add(self, data):
    if self.size >= self.capacity:
      self.grow()
    
    self.array[self.size] = data
    self.size += 1

  def insert(self, index, data):
    if self.size >= self.capacity:
      self.grow()
    
    for i in range(self.size, index, -1):
      self.array[i] = self.array[i-1]
    self.array[index] = data
    self.size += 1

  def delete(self, data):
    # my version
    for i in range(self.size):
      if self.array[i] == data:
        for j in range(i, self.size-1):
          self.array[j] = self.array[j+1]
        self.array[self.size-1] = '<empty_cell>'
        self.size -= 1

        if self.size < int(self.capacity / 3):
          self.shrink()
        
        break

    # bro version
    # for i in range(self.size):
    #   if self.array[i] == data:
    #     for j in range(self.size - i - 1):
    #       self.array[i + j] = self.array[i + j + 1]
    #     self.array[self.size - 1] = '<empty_cell>'
    #     self.size -= 1

    #     if(self.size <= int(self.capacity / 3)):
    #       self.shrink()
    #     break

  def search(self, data):
    for i in range(self.size):
      if self.array[i] == data:
        return i
    return -1
  
  def grow(self):
    self.newCapacity = self.capacity * 2
    self.newArray = ['<empty_cell>' for i in range(self.newCapacity)]
    
    for i in range(self.size):
      self.newArray[i] = self.array[i]
    
    self.capacity = self.newCapacity
    self.array = self.newArray

  def shrink(self):
    self.newCapacity = int(self.capacity / 2)
    self.newArray = ['<empty_cell>' for i in range(self.newCapacity)]
    
    for i in range(self.size):
      self.newArray[i] = self.array[i]
    
    self.capacity = self.newCapacity
    self.array = self.newArray
    

  def isEmpty(self):
    return len(self.array) == 0

  def toString(self):
    return '[' + ', '.join([ str(i) for i in self.array ]) + ']'


da = DynamicArray()


for i in range(15):
  da.add(i)

print(da.toString())
print(f'size: {da.size}')
print(f'capacity: {da.capacity}')
print('empty: ' + str(da.isEmpty()))

print('Data was found at index={}'.format(da.search('2')))

for i in range(da.size, 3, -1):
  da.delete(i)

print(da.toString())
print(f'size: {da.size}')
print(f'capacity: {da.capacity}')
print('empty: ' + str(da.isEmpty()))
