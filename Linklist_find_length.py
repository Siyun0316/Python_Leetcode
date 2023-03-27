#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:21:58 2023

@author: siyun
"""

# length of the ListNode recrusion
class ListNode(object):
    def __init__ (self, val):
        self.val = val
        self.next = None

class Solution(object):
    def findLength(self, head):
        if not head:
            return 0
        return self.findLength(head.next)+1

# time & space O(n)