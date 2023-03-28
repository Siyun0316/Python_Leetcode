class Listnode(object):
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution(object):
    def quickSort(self, head):
        if not head or not head.next:
            return head
        tail = self.findTail(head)
        head,tail = self.sort(head,tail)
        tail.next ##cut cycle
        return head

    def sort(self,head,tail):
        if not head or not tail or head == tail:
            return head, tail
        lhead, ltail, rhead, rtail, ref_head, ref_tail = self.partition(head,tail)
        if not lhead:  # if there is no node in left part
            head = ref_head
        else:
            head, ltail = self.sort(lhead,ltail)
            ltail.next = ref_head
        if not rhead:  # if there is no node in left part
            tail = ref_tail
        else:
            rhead,tail = self.sort(rhead,rtail)
            ref_tail.next = rhead
        return head, tail

    def partition(self, head,tail):
        lhead,ltail,rhead,rtail = None,None,None,None
        ref_head,ref_tail = tail,tail ## reference partition tail
        if not head or head == tail:
            return lhead,ltail,rhead,rtail,ref_head,ref_tail
        cur = head
        while cur != tail:
            if cur.val < tail.val:
                if not lhead:
                    lhead,ltail = cur,cur
                else:
                    ltail.next = cur
                    ltail = ltail.next
            elif cur.val == tail.val:
                ref_tail.next = cur
                ref_tail = ref_tail.next
            else:
                if not rhead:
                    rhead,rtail = cur,cur
                else:
                    rtail.next = cur
                    rtail = rtail.next
            cur = cur.next
        return lhead,ltail,rhead,rtail,ref_head,ref_tail

    def findTail(self,head):
        while head.next:
            head = head.next
        return head

# time complexity O(nlogn)
# space complexity O(logn)


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
'''
class Linklist(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def append(self,val):
        if not self.head:
            self.head = self.tail = Listnode(val)
            return
        newnode = Listnode(val)
        self.tail.next = newnode
        self.tail = self.tail.next
        return

    def size(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return "None"
        strs = []
        cur = self.head
        while cur:
            strs.append(str(cur.val))
            cur = cur.next
        return "->".join(strs)
        '''
# test

test_hd = Listnode(1)
test_c = Linklist()
test_b = Linklist()

for i in range(10):
    if i%2 ==0:
        test_c.append(i+4)
    else:
        test_c.append(i*2+1)

print(test_c)
c = Solution().quickSort(test_c.head)
sorted_list = Linklist()
sorted_list.head = c
print(sorted_list)

print(test_b)
b = Solution().quickSort(test_b.head)
sorted_list = Linklist()
sorted_list.head = b
print(sorted_list)