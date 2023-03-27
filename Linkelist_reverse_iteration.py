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
class Linklist:
    def __init__(self,head):
        self.head = None
        self.next = None
        
    def display(self):
        self.display_helper(self.head)
 
    def display_helper(self, current):
        if current is None:
            return
 
        print(current.data, end = ' ')
        self.display_helper(current.next)
 

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


# tests

test_hd = Listnode(1)
test_c = test_hd
for i in range(10):    
    test_c.next = Listnode((i%2)+1)
    test_c = test_c.next

a = Solution().reverse(Listnode(2))
b = Solution().reverse(None)
c = Solution().reverse(test_hd)

a.display()
b.display()
c.display()
