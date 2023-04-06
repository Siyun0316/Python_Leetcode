# 612. Design Linked List
# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if not self.head:
            return "None"
        cur = self.head
        strs = []
        while cur:
            strs.append(str(cur.val))
            cur = cur.next
        return '->'.join(strs)

    def __get (self, index):
        '''
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: int
        :return: ListNode
        '''
        if index < 0 or self.size <= index:
            return None
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur

    def get(self,index):
        '''
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: int
        :return: int
        '''
        cur_node = self.__get(index)
        return cur_node.val if cur_node else -1

    def addAtHead(self,val):
        '''
        :param val: int
        :return:
        '''
        if not self.head:
            self.head = self.tail = ListNode(val)
        else:
            newNode = ListNode(val)
            newNode.next = self.head
            self.head = newNode
        self.size +=1
        return

    def addAtTail(self,val):
        '''
        :param val: int
        :return:
        '''
        if not self.head:
            self.head = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        self.size +=1
        return

    def isEmpty(self):
        '''
        :return: boolean
        '''
        return self.size == 0

    def addAtIndex(self,index,val):
        '''
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :param index: int
        :param val: int
        :return:
        '''
        if index < 0 or self.size < index:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)
        pre = self.__get(index-1)
        tmp = pre.next
        newNode = ListNode(val)
        newNode.next = tmp
        pre.next = newNode
        self.size +=1
        return

    def deleteAtIndex(self,index):
        '''
        Delete the index-th node in the linked list, if the index is valid.
        :param index: int
        :return:
        '''
        if index < 0 or self.size <= index:
            return
        if index == 0 and self.size >1:
            newhead = self.head.next
            self.head.next = None
            self.head = newhead
            self.size -=1
            return
        if index == 0 and self.size == 1:
            self.head = self.tail = None
            self.size -=1
            return
        pre = self.__get(index - 1)
        remove_node = pre.next
        pre.next = remove_node.next
        remove_node.next = None

        if index + 1 == self.size:
            self.tail = pre

        self.size -=1
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





