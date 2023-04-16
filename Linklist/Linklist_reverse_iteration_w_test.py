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
        
class Linklist(object):
    def __init__(self):
        self.head = None
        self.next = None
        self.last_node = None
        
    def append(self, data):
        if self.last_node is None:
            self.head = Listnode(data)
            self.last_node = self.head
        else:
            self.last_node.next = Listnode(data)
            self.last_node = self.last_node.next
            
    def reverse(self):
        if not self.head or not self.head.next:
            return self.head 
        pre, cur = None,self.head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur,tmp
        self.head = pre
    
    def __str__(self):
        if not self.head:
            return "None"
        strs = []
        cur = self.head
        while cur:
            strs.append(str(cur.val))
            cur = cur.next
        return "->".join(strs)

 

#time complexity O(n)
#space complexity O(1)


# tests

b_list = Linklist()
a_list = Linklist()
c_list = Linklist()
for i in range(10):
    a_list.append((i%3)+1)    

b_list.append(1)

print("list_a before reverse is ")
print(a_list)
print("\nlist_b before reverse is ")
print(b_list)
print("\nlist_c before reverse is ")
print(c_list)

a_list.reverse()
b_list.reverse()
c_list.reverse()

print("\nlist_a after reverse is ")
print(a_list)
print("\nlist_b after reverse is ")
print(b_list)
print("\nlist_c after reverse is ")
print(c_list)

