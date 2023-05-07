# Reverse Linked List In Pairs
# Reverse pairs of elements in a singly-linked list.
# Examples
# L = null, after reverse is null
# L = 1 -> null, after reverse is 1 -> null
# L = 1 -> 2 -> null, after reverse is 2 -> 1 -> null
# L = 1 -> 2 -> 3 -> null, after reverse is 2 -> 1 -> 3 -> null

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseInPairs(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, dummy.next
        # pre, cur , _next, tmp
        # pre, _next, cur, tmp
        while cur and cur.next:
            tmp = cur.next.next
            _next = cur.next
            pre.next = _next
            _next.next = cur
            cur.next = tmp
            pre = cur
            cur = cur.next
        return dummy.next

# time complexity O(n)
# space complexity O(1)

# Test case 1: empty list
head = None
sol = Solution()
assert sol.reverseInPairs(head) == None

# Test case 2: list with a single node
head = ListNode(1)
sol = Solution()
result = sol.reverseInPairs(head)
assert result.val == 1
assert result.next == None

# Test case 3: list with an odd number of nodes
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
sol = Solution()
result = sol.reverseInPairs(head)
assert result.val == 2
assert result.next.val == 1
assert result.next.next.val == 3
assert result.next.next.next == None

# Test case 4: list with an even number of nodes
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
result = sol.reverseInPairs(head)
assert result.val == 2
assert result.next.val == 1
assert result.next.next.val == 4
assert result.next.next.next.val == 3
assert result.next.next.next.next == None


