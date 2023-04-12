# 44. Pre-order Traversal Of Binary Tree (iterative)
#

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def preOrder(self, root):
        '''
        :param root: TreeNode
        :return: list[int]
        '''
        if not root:
            return []
        tmp = [(root, 1)]
        res = []
        while tmp:
            cur,cnt = tmp.pop()
            if cnt==1 :
                res.append(cur.val)
                tmp.append((cur, cnt+1))
                if cur.left:
                    tmp.append((cur.left, 1))
            if cnt ==2 :
                if cur.right:
                    tmp.append((cur.right, 1))
        return res

# time complexity O(n)
# space complexity O(height)

# Test case 1
#      1
#     / \
#    2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().preOrder(root))


# Test case 2
#      1
#       \
#        2

root = TreeNode(1)
root.right = TreeNode(2)
print(Solution().preOrder(root))


# Test case 3
#      1
#     / \
#    2   3
#       / \
#      4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(Solution().preOrder(root))


# Test case 4
# Output: []

print(Solution().preOrder(None))