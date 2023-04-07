# 612. Design Linked List
# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
    def __str__(self):
        return 'ListNode({})'.format(str(self.val))

def link_between(mid, prev, next):
    mid.next = next
    mid.prev = prev
    prev.next = mid
    next.prev = mid

def unlink_between(mid, prev, next):
    mid.next = mid.prev = None
    prev.next = next
    next.prev = prev

class LinkList(object):
    def __init__(self):
        self.before_head = ListNode(None)
        self.after_tail = ListNode(None)
        self.before_head.next = self.after_tail
        self.after_tail.prev = self.before_head
        self.size = 0

    def __str__(self):
        if not self.before_head.next:
            return "None"
        cur = self.before_head.next
        strs = []
        while cur:
            strs.append(str(cur.val))
            cur = cur.next
        return '->'.join(strs)

    def _get(self,indx):
        '''
        Get the value of the index-th node in the linked list. If the index is invalid, return None.
        :param index: int
        :return: ListNode
        '''
        if indx < 0 or self.size <= indx:
            return None
        cur = self.before_head.next
        for i in range(indx):
            cur = cur.next
        return cur

    def get(self,indx):
        '''
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: int
        :return: int
        '''
        node = self._get(indx)
        return node.val if node else -1

    def addAtHead(self,val):
        '''
        :param val: int
        :return:
        '''
        link_between(ListNode(val),self.before_head,self.before_head.next)
        self.size +=1
        return

    def addAtTail(self,val):
        '''
        :param val: int
        :return:
        '''
        link_between(ListNode(val), self.after_tail.prev, self.after_tail)
        self.size +=1
        return

    def isEmpty(self):
        '''
        :return: boolean
        '''
        return self.size == 0

    def addAtIndex(self,indx,val):
        '''
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :param index: int
        :param val: int
        :return:
        '''
        if indx < 0 or self.size < indx:
            return
        if indx == 0:
            return self.addAtHead(val)
        if indx == self.size:
            return self.addAtTail(val)
        node = self._get(indx)
        link_between(ListNode(val),node.prev,node)
        self.size +=1
        return

    def deleteAtIndex(self,indx):
        '''
        Delete the index-th node in the linked list, if the index is valid.
        :param index: int
        :return:
        '''
        if indx < 0 or self.size <= indx:
            return
        node = self._get(indx)
        unlink_between(node,node.prev,node.next)
        self.size -= 1
        return


test_c = LinkList()

print(test_c)

test_c.addAtHead(2)
test_c.addAtTail(3)
test_c.addAtTail(4)
test_c.addAtIndex(3,5)
test_c.addAtTail(6)
test_c.addAtTail(7)
test_c.deleteAtIndex(2)
test_c.isEmpty()


print(test_c)

test_c.deleteAtIndex(0)
print(test_c)

print(test_c.deleteAtIndex(7))
print(test_c)

test_c.deleteAtIndex(3)
print(test_c)