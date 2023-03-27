#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:54:41 2023

@author: siyun
"""

# merge sort the unknown length linklist 

class Listnode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        l_head,r_head = self.split(head)
        lh = self.mergeSort(l_head)
        rh = self.mergeSort(r_head)
        return self.merge(lh,rh)
    

    def split(self,head):
        if not head or not head.next:
            return head, head
        pre, s, f= head, head, head
        while f and f.next:
            pre = s
            s = s.next
            f = f.next.next
            pre.next =None
        return head, s

    def merge(self,lh, rh):
        dummy = Listnode(None)
        cur = dummy
        while lh or rh:
            if not rh:
                cur.next = lh
                break
            if not lh:
                cur.next = rh
                break
            if rh.val > lh.val:
                cur.next = lh
                lh = lh.next
            else:
                cur.next = rh
                rh = rh.next
            cur = cur.next
        return dummy.next

# Time complexity O(nlogn)
# Space complexity O(logn)
        
