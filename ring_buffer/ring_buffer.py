class RingBuffer:

    counter = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):

        if len(self.storage) == self.capacity:
            self.storage[self.index] = item

        else:
            self.storage.append(item)

        # add item to the index after the one it's at
        self.index = (self.index + 1) % self.capacity
    

    def get(self):
        ''' Returns all elements in the buffer 
        as a list in their given order
        '''
        return self.storage


# buffer = RingBuffer(3)

# buffer.get()

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()  

# buffer.append('d')

# buffer.get()   

# buffer.append('e')
# buffer.append('f')

# buffer.get() 

buffer = RingBuffer(5)
buffer.append('a')
print(buffer.get())