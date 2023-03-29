# Merge K sorted lists into one big sorted list in ascending order.
# ListOfLists is not null, and none of the lists is null.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

import heapq

class Solution(object):
  def merge(self, nodes):
    """
    input: ListNode[] nodes
    return: ListNode
    """
    tmp_h = []
    k = len(nodes)
    for i in range(k):
      if nodes[i]:
        tmp_h.append((nodes[i].val, i))
        nodes[i] = nodes[i].next
    heapq.heapify(tmp_h)
    dummy = ListNode(-1)
    cur = dummy
    while tmp_h:
      val,  index = heapq.heappop(tmp_h)
      cur.next = ListNode(val)
      cur = cur.next
      if nodes[index]:
        heapq.heappush(tmp_h,(nodes[index].val, index) )
        nodes[index] = nodes[index].next
    return dummy.next
# time complexity O(nklog(k)) k = len(nodes)
# space complexity O(k)

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

  def append(self, val):
    if not self.head:
      self.head = self.tail = ListNode(val)
      return
    newnode = ListNode(val)
    self.tail.next = newnode
    self.tail = self.tail.next
    return

test_a = Linklist()
test_b = Linklist()
test_c = Linklist()

for i in range(10):
    test_b.append(i*2+1)
    test_c.append(i+3)
print(test_a)
print(test_b)
print(test_c)
a = Solution().merge([test_a.head,test_a.head])
sorted_list2 = Linklist()
sorted_list2.head = a
print(sorted_list2)
c = Solution().merge([test_b.head,test_c.head])
sorted_list1 = Linklist()
sorted_list1.head = c
d= Solution().merge([test_b.head, test_b.head,test_c.head])
sorted_list3 = Linklist()
sorted_list3.head = d
print(sorted_list1)
# inplace edit the input linkedlist
print(sorted_list3)
