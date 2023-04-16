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
    
    def append(self,val):
        if not self.head:
            self.head = self.tail = Listnode(val)
            return
        newnode = Listnode(val)
        self.tail.next = newnode
        self.tail = self.tail.next
        return 

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
            return head, None
        s, f= head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s.next
        s.next = None
        return head, mid

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

#tests
'''
test_hd = Listnode(1)
test_c = Linklist()

print(test_c)
c = Solution().mergeSort(test_c.head)
sorted_list = Linklist()
sorted_list.head = c
print(sorted_list)

for i in range(10):
    if i == 0:
        test_c.append(i+4)
        print(test_c)
        c = Solution().mergeSort(test_c.head)
        sorted_list = Linklist()
        sorted_list.head = c
        print(sorted_list)
    if i%2 ==0:
        test_c.append(i+4)
    else:
        test_c.append(i*2+1)

print(test_c)
c = Solution().mergeSort(test_c.head)
sorted_list = Linklist()
sorted_list.head = c
print(sorted_list)
'''

        
