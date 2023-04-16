# 60. Height of Binary Tree
# Find the height of binary tree.

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findHeight(self,root):
        if not root:
            return 0
        l_height = self.findHeight(root.left)
        r_height = self.findHeight(root.right)
        return max(l_height,r_height)+1

# time complexity O(n)
# space complexity O(height) O(logn)~O(n)

#   3
#  / \
# 9  20
#   /  \
#  15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().findHeight(root))

#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
root.right.right.right.right = TreeNode(5)

print(Solution().findHeight(root))

#    1
#   / \
#  2   3


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(Solution().findHeight(root))