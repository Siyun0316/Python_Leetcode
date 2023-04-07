#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:25:59 2023

@author: siyun
"""

# Desgin Linked list
# get index val, get index node, add at head, add at tail
# add at index, delete at index, is empty
class Listnode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def __init__(self):
        self._head = None
        self.size = 0
        self._tail = None
    #s O(1) t O(n)
    # get index node
    def _get (self, index):
        if self.size-1 < index:
            return
        cur = self._head
        for i in range(index):
            cur = cur.next
        return cur
    #s O(1) t O(n)
    # get index val
    def get(self, index):
        if self.size-1 < index:
            return -1
        return self._get(index).val
    #s O(1) t O(1)
    # check empty
    def isEmpty(self):
        return self.size == 0
    #s O(1) t O(1)
    # add at head
    def addHead(self, val):
        if self.isEmpty():
            self._head = self._tail = Listnode(val)
            self.size +=1
            return
        newnode = Listnode(val)
        newnode.next = self._head
        self._head = newnode
        self.size +=1
        return
    # add at tail
    #s O(1) t O(1)
    def addTail(self,val):
        if self.isEmpty():
            self._head = self._tail = Listnode(val)
            self.size +=1
            return
        self._tail.next = Listnode(val)
        self._tail = self._tail.next
        self.size +=1
        return

    #s O(1) t O(n)
    # add at index position
    def addIndex(self, index, val):
        if self.size == index:
            return self.addTail(val)
        if self.size < index or index <0:
            return 
        if index == 0:
            return self.addHead(val)
        pre = self._get(index-1)
        newnode = Listnode(val)
        tmp = pre.next
        pre.next = newnode
        newnode.next = tmp
        self.size +=1
        return
    #s O(1) t O(n)
    # remove index postion
    def deleteIndex(self, index):
        if self.size <= index or index <0:
            return
        if index == 0:
            if self.size ==1:
                self._head = self._tail = None
            else:
                newhead = self._head.next
                self._head.next = None
                self._head = newhead
            self.size -=1
            return
        if index == self.size -1:
            self._tail = self._get(index-1)
            self.size -=1
            return
        pre = self._get(index-1)
        remove = pre.next
        pre.next = remove.next
        remove.next = None
        self.size -=1
        return
    
    def __str__(self):
        strs = []
        node = self._head
        while node:
            strs.append(str(node.val))
            node = node.next
        return "->".join(strs)
        


# tests


a_list = Solution()
print(a_list.isEmpty())
a_list.addHead(1)
a_list.addHead(2)
a_list.addHead(3)
a_list.addTail(4)
a_list.addTail(5)
a_list.addIndex(4, 6)
a_list.addIndex(4, 7)
a_list.deleteIndex(10)
a_list.deleteIndex(1)

print(a_list)
print(a_list.get(2))
print(a_list.get(5))
print(a_list.get(6))
print(a_list.isEmpty())





