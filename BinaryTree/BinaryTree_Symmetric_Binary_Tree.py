# 48. Symmetric Binary Tree
# Check if a given binary tree is symmetric.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        input: TreeNode root
        return: boolean
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, lf, rt):
        if not lf and not rt:
            return True
        if not lf or not rt or lf.val != rt.val:
            return False
        return (self.helper(lf.left, rt.right)) and (self.helper(lf.right, rt.left))

# time complexity O(n)
# space complexity O(height) O(logn)~O(n)

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))

#     1
#    / \
#   2   2
#    \   \
#    3    3
#

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))

#     1
#    / \
#   2   2
#    \
#     3
#
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)

print(Solution().isSymmetric(root))





