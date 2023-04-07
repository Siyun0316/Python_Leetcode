# 613. Design Circular Deque
# Design your implementation of the circular double-ended queue (deque).
# Your implementation should support following operations:
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return -1.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.


class CircularDeque(object):
    # MyCircularDeque(k): Constructor, set the size of the deque to be k.
    def __init__(self,k):
        self.front = 0
        self.end = 1
        self.size = 0
        self.que = [None]*(k+1)
        self.length = k +1
    def __str__(self):
        if self.isEmpty():
            return "None"
        return ','.join(str(x) for x in self.que if x is not None)

    # isEmpty(): Checks whether Deque is empty or not.
    def isEmpty(self):
        return self.size == 0

    # isFull(): Checks whether Deque is full or not.
    def isFull(self):
        return self.size == self.length -1

    # getRear(): Gets the last item from Deque. If the deque is empty, return -1.
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.que[(self.end-1+self.length)%self.length]

    # getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.que[(self.front+1)%self.length]

    # insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
    def insertFront(self, val):
        if self.isFull():
            return False
        self.que[self.front] = val
        self.front = (self.front-1+self.length)%self.length
        self.size +=1
        return True

    # insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
    def insertLast(self,val):
        if self.isFull():
            return False
        self.que[self.end] = val
        self.end = (self.end + 1)%self.length
        self.size +=1
        return True

    # deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
    def deletFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front+1)%self.length
        self.que[self.front] = None # for test QC
        self.size -= 1
        return True

    # deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
    def deleteLast(self):
        if self.isEmpty():
            return False
        self.end = (self.end-1+self.length)%self.length
        self.que[self.end] = None  # for test QC
        self.size -= 1
        return True

# time complexity O(1)
# space complexity O(k) or O(k)

test = CircularDeque(5)
print(test.isEmpty())
test.insertFront(1)
print(test)
test.insertFront(2)
print(test)
test.insertFront(3)
print(test)
print(test.getRear())
test.insertLast(4)
print(test)
test.insertLast(5)
print(test)
test.insertLast(6)
print((test.isFull()))
print(test)
test.deleteLast()
test.deletFront()
print(test)

