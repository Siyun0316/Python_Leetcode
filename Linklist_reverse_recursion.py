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