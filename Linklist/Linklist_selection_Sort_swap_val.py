
# selection sort: swap value method
class Listnode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def selectionSort(self, head):
        if not head or not head.next:
            return head
        dummy = Listnode(-1)
        dummy.next = head
        tail = dummy
        while tail.next:
            pre,cur = tail, tail.next
            pre_min,cur_min = pre, cur
            while cur:
                if cur_min.val > cur.val:
                    pre_min, cur_min = pre, cur
                pre, cur = cur, cur.next
            pre_min.next = cur_min.next
            tmp = tail.next
            tail.next = cur_min
            cur_min.next = tmp
            tail = tail.next
        return dummy.next
# time complexity O(n^2)
# space complexity O(1)


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

test_hd = Listnode(1)
test_c = Linklist()


for i in range(10):
    if i%2 ==0:
        test_c.append(i+4)
    else:
        test_c.append(i*2+1)

print(test_c)
c = Solution().selectionSort(test_c.head)
sorted_list = Linklist()
sorted_list.head = c
print(sorted_list)