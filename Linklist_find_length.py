#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:21:58 2023

@author: siyun
"""

# length of the ListNode
class ListNode(object):
    def __init__ (self, val):
        self.val = val
        self.next = None
        
def solution(self, head):
        if not head:
            return 0
        return self.solution(head.next)+1
