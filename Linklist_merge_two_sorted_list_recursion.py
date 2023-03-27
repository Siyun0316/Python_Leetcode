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