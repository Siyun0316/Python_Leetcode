#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:03:00 2023

@author: siyun
"""

# Reverse Link list iterative
class Listnode(object):
    def __init__(self,val):
        
        self.val = val
        self.next = None

class Linklist(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        strs = []
        node = self.head
        while node:
            strs.append(str(node.val))
            node = node.next
        return "->".join(strs)

    def append(self, val):
        if not self.head:
            self.head = self.tail = Listnode(val)
            return
        newnode = Listnode(val)
        self.tail.next = newnode
        self.tail = self.tail.next
        return

class Solution(object):
    def reverse(self,head):
        if not head or not head.next:
            return head 
        pre, cur = None,head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur,tmp
        return cur

#time complexity O(n)
#space complexity O(1)


#test
'''
class Linklist(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        strs = []
        node = self.head
        while node:
            strs.append(str(node.val))
            node = node.next
        return "->".join(strs)

    def append(self, val):
        if not self.head:
            self.head = self.tail = Listnode(val)
            return
        newnode = Listnode(val)
        self.tail.next = newnode
        self.tail = self.tail.next
        return

test_a = Linklist()
test_b = Linklist()
test_c = Linklist()

for i in range(10):
    test_b.append(i*2+1)
    test_c.append(i+3)
print(test_a)
print(test_b)
print(test_c)
a = Solution().reverse(test_a.head)
sorted_list = Linklist()
sorted_list.head = a
print(sorted_list)
b = Solution().reverse(test_b.head)
sorted_list = Linklist()
sorted_list.head = b
print(sorted_list)
c = Solution().reverse(test_c.head)
sorted_list = Linklist()
sorted_list.head = c
print(sorted_list)
'''

