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

