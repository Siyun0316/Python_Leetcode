# 126. Lowest Common Ancestor I
# Given two nodes in a binary tree, find their lowest common ancestor.
# Assumptions
# There is no parent pointer for the nodes in the binary tree
# The given two nodes are guaranteed to be in the binary tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right

# time complexity O(n)
# space complexity O(height)

# Test Case 1
#       3
#      / \
#     5   1
#    / \   \
#   6   2   8
#      / \
#     7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.right = TreeNode(8)
assert Solution().lowestCommonAncestor(root, root.left, root.right) == root

# Test Case 2
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
assert Solution().lowestCommonAncestor(root, root.left, root.right) == root

# Test Case 3
#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
assert Solution().lowestCommonAncestor(root, root.left.left, root.right.left) == root

# Test Case 4
#   2
#  / \
# 1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert Solution().lowestCommonAncestor(root, root.left, root.right) == root

# Test Case 5
#   1
#  / \
# 2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
assert Solution().lowestCommonAncestor(root, root.right, root.right.right) == root.right

# Test Case 6
#   1
#  / \
# 2   3
#  \
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
assert Solution().lowestCommonAncestor(root, root.left.right, root.right) == root
