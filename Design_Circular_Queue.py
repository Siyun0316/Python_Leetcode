# 614. Design Circular Queue
# The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle
# and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.

class CircularQueue(object):
    def __init__(self,k):
        self.items = [None]*(k+1)
        self.head = 0
        self.tail = 0
        self.size = 0
        self.length = k+1

    def __str__(self):
        if self.size == 0:
            return 'None'
        return ','.join(str(x) for x in self.items if x is not None)

    # isEmpty(): Checks whether the circular queue is empty or not.
    def isEmpty(self):
        return self.size == 0

    # isFull(): Checks whether the circular queue is full or not.
    def isFull(self):
        return self.size == self.length -1

    # Front: Get the front item from the queue. If the queue is empty, return -1.
    def Front(self):
        if self.isEmpty():
            return -1
        return self.items[self.head]

    # Rear: Get the last item from the queue. If the queue is empty, return -1.
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.items[(self.tail -1 +self.length)%self.length]

    # enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
    def enQueue(self,val):
        if self.isFull():
            return False
        self.items[self.tail] = val
        self.tail = (self.tail +1)%self.length
        self.size +=1
        return True

    # deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
    def deQueue(self):
        if self.isEmpty():
            return False
        self.items[self.head] = None
        self.head = (self.head +1)%self.length
        self.size -=1
        return True

# time complexity O(1)
# space complexity O(k) or O(1)

test = CircularQueue(5)
print(test.isEmpty())
print(test.isFull())
test.enQueue(1)
test.enQueue(2)
test.enQueue(3)
test.enQueue(4)
print(test)
print(test.Front())
print(test.Rear())
print(test.deQueue())




