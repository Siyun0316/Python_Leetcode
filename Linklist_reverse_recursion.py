#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:36:07 2023

@author: siyun
"""

# Reverse Linked List (recursive)

class Listnode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def reverse(self,head):
        if not head or not head.next:
            return head
        newhead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newhead

#Time complexity O(n)
#space complexity O(n)


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