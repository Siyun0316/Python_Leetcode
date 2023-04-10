# 46. Check If Binary Tree Is Balanced
# Check if a given binary tree is balanced. A balanced binary tree is one in which
# the depths of every node’s left and right subtree differ by at most 1.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        '''
        :param root: TreeNode
        :return: boolean
        '''
        if not root:
            return True
        def height(node):
            if not node:
                return 0
            return max(height(node.left),height(node.right))+1
        if abs(height(root.left) - height(root.right)) >1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

# time complexity O(n)
# space complexity O(height)

# Test case 1
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
assert Solution().isBalanced(root) == True

# Test case 2
#       1
#      /
#     2
#    /
#   3
#  /
# 4
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
assert Solution().isBalanced(root) == False



