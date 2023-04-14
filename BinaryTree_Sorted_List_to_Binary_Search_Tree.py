# Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# For testing purpose, please make sure for any node in the result,
# its left sub-tree should have equal or only one more node than its right sub-tree.
# Example:
#     Given ascending order list: 1→3→4→5→8→11
#
#     return Binary Search Tree is
#
#               5
#
#           /        \
#
#         3          11
#
#     /      \      /
#
#   1        4    8

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        input: ListNode head
        return: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        lhead, newroot, rhead = self.findMid(head)
        root = TreeNode(newroot.val)
        root.left = self.sortedListToBST(lhead)
        root.right = self.sortedListToBST(rhead)
        return root


    def findMid(self,head):
        if not head or not head.next:
            return head
        pre, s,f = head, head, head
        while f and f.next:
            pre = s
            s = s.next
            f = f.next.next
        pre.next = None
        return head, s, s.next


# time complexity O(nlogn)
# space complexity O(logn)

    def sortedListToBST2(self, head):
        """
        input: ListNode head
        return: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return self.createBST(arr)
    def createBST(self, arr):
        if not arr:
            return None
        mid = (len(arr))//2
        root = TreeNode(arr[mid])
        root.left = self.createBST(arr[:mid])
        root.right = self. createBST(arr[mid+1:])
        return root

# time complexity O(n)
# space complexity O(n)


def printLayer(root):
    """
    input: TreeNode root
    return: Integer[]
    """
    if not root:
        return []
    res = []
    tmp = [root]
    while tmp:
        cur_lvl = len(tmp)
        line = []
        for i in range(cur_lvl):
            cur = tmp.pop(0)
            line.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        res.append(line)
    return res

def print_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next

# test case 1
linked_list = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(8, ListNode(11))))))
print_list(linked_list)
# Expected output:
#     5
#   /   \
#   3    11
#  / \   /
# 1   4  8
root = Solution().sortedListToBST2(linked_list)
print(printLayer(root))
# the findMid() changes the object.next, inplace split the link link list
root = Solution().sortedListToBST(linked_list)
print(printLayer(root))


# Test case 2:
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(linked_list)
# Expected output:
#   3
#  /
#  2  5
# /
# 1
#
root = Solution().sortedListToBST2(linked_list)
print(printLayer(root))
# the findMid() changes the object.next, inplace split the link link list
root = Solution().sortedListToBST(linked_list)
print(printLayer(root))


# Test case 3:
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print_list(linked_list)
# Expected output:
#      4
#    /  \
#   2    6
#  / \  /
# 1   3 5
#
root = Solution().sortedListToBST2(linked_list)
print(printLayer(root))
# the findMid() changes the object.next, inplace split the link link list
root = Solution().sortedListToBST(linked_list)
print(printLayer(root))
