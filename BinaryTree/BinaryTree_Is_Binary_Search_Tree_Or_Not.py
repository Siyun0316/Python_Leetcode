# 54. Is Binary Search Tree Or Not
# Determine if a given binary tree is binary search tree.
# There should no be duplicate keys in binary search tree.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBST(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        if not root:
            return True
        def helper(root, _min, _max):
            if not root:
                return True
            if root.val >= _max or root.val <= _min:
                return False
            return helper(root.left, _min, root.val) and helper(root.right, root.val, _max)
        return helper(root, float('-inf'), float('inf'))

# time complexity O(n)
# space complexity O(height)

# Test Case 1
#     2
#    / \
#   1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert Solution().isBST(root) == True

# Test Case 2
#     5
#    / \
#   1   4
#      / \
#     3   6
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
assert Solution().isBST(root) == False

# Test Case 3
#     5
#    / \
#   3   8
#  / \   \
# 1   4  10
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(10)
assert Solution().isBST(root) == True

# Test Case 4
#     5
#    / \
#   4   7
#  /   / \
# 3   6   8
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(7)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
assert Solution().isBST(root) == True


