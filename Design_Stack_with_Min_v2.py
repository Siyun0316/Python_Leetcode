# 32. Stack With min()
# Enhance the stack implementation to support min() operation. min() should return the current minimum value in the stack.
# If the stack is empty, min() should return -1.
# push(int element) - push the element to top
# pop() - return the top element and remove it, if the stack is empty, return -1
# top() - return the top element without remove it, if the stack is empty, return -1
# min() - return the current min value in the stack.

class Stack(object):
    def __init__(self):
        self._list = []
        self._min = []
        self.size = 0

    # push(int element) - push the element to top
    def push(self,val):
        self._list.append(val)
        if self.size == 0 or self._min[-1] >= val:
            self._min.append(val)
        self.size +=1
        return

    # pop() - return the top element and remove it, if the stack is empty, return -1
    def pop(self):
        if self.size == 0:
            return -1
        if self._min[-1] == self._list[-1]:
            self._min.pop()
        return self._list.pop()

    # top() - return the top element without remove it, if the stack is empty, return -1
    def top(self):
        if self.size == 0:
            return -1
        return self._list[-1]

    # min() - return the current min value in the stack.
    def min(self):
        if self.size == 0:
            return -1
        return self._min[-1]

# time complexity O(1)
# space complexity O(n) less than O(2n)

test = Stack()
print(test.push(1))
print(test.push(2))
test.push(3)
test.push(4)
test.push(0)
test.push(1)
print(test._list)
print(test.min())
test.pop()
print(test.min())
test.pop()
print(test.min())
print(test._list)
test.pop()
print(test.min())
print(test._list)
print(test._min)
test.pop()
print(test.min())
print(test._list)
test.pop()
print(test.min())
print(test._list)
print(test._min)
print(test.top())