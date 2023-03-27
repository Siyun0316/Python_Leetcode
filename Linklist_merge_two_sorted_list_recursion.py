#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:37:36 2023

@author: siyun
"""

# Merge Two Sorted Linked Lists

class Listnode(object):
    def __init__ (self,val):
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
    def merge(self,lh,rh):
        if not lh:
            return rh
        if not rh:
            return lh
        if lh.val < rh.val:
            lh.next = self.merge(lh.next,rh)
            return lh
        else:
            rh.next = self.merge(rh.next,lh)
            return rh
# Time complexity O(len(lh) + len(rh))

# Space complexity O(len(lh) + len(rh))

#test
'''
test_a = Linklist()
test_b = Linklist()
test_c = Linklist()

for i in range(10):
    test_b.append(i*2+1)
    test_c.append(i+3)
print(test_a)
print(test_b)
print(test_c)
a = Solution().merge(test_b.head,test_a.head)
sorted_list2 = Linklist()
sorted_list2.head = a
print(sorted_list2)
c = Solution().merge(test_b.head,test_c.head)
sorted_list1 = Linklist()
sorted_list1.head = c
print(sorted_list1)
# inplace edit the input linkedlist 
print(sorted_list2)
'''