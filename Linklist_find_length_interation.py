#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:22:54 2023

@author: siyun
"""

# length of the ListNode iteration
class ListNode(object):
    def __init__ (self, val):
        self.val = val
        self.next = None

class Solution(object):
    def findLength(self,head):
        if not head:
            return 0
        count = 0
        while head:
            count +=1
            head= head.next
        return count

# time complexity O(n)
# space complexity O(1)

# tests
'''
test_hd = ListNode(1)
test_c = test_hd
for i in range(10):    
    test_c.next = ListNode((i%2)+1)
    test_c = test_c.next

a = Solution().findLength(ListNode(2))
b = Solution().findLength(None)
c = Solution().findLength(test_hd)
print (str(a) + ", " + str(b) + "," + str(c))
'''