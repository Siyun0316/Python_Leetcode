# 33. Number Of Nodes
# Return the number of nodes in the linked list.

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None

    def __str__(self):
        if not self.head:
            return "None"
        strs = []
        cur = self.head
        while cur:
            strs.append(str(cur.val))
        return "->".join(strs)

    def append(self,val):
        if not self.head:
            self.head = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        return

class Solution(object):
    def numOfNodes(self,head):
        '''
        :param head: ListNode head
        :return: int
        '''
        if not head:
            return 0
        count = 0
        while head:
            count +=1
            head = head.next
        return count

# time complexity O(n)
# space complexity O(1)

test_c = LinkList()

print(test_c)
c = Solution().numOfNodes(test_c.head)
print(c)

for i in range(11):
    if i == 0:
        test_c.append(i+4)
    elif i%2 ==0:
        test_c.append(i+4)
    else:
        test_c.append(i*2+1)

c = Solution().numOfNodes(test_c.head)
print(c)

