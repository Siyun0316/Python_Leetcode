# 449. Invert Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invert(self, root):
        if not root or (not root.left and not root.right):
            return root

        rt = self.invert(root.right)
        lf = self.invert(root.left)

        root.left = rt
        root.right = lf

        return root

# time complexity O(n)
# space complexity O(height)


# Test Case 1
#         4                   4
#       /   \               /   \
#      2     7     =>      7     2
#     / \   / \           / \   / \
#    1   3 6   9         9   6 3   1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
inverted = solution.invert(root)

assert inverted.val == 4
assert inverted.left.val == 7
assert inverted.right.val == 2
assert inverted.left.left.val == 9
assert inverted.left.right.val == 6
assert inverted.right.left.val == 3
assert inverted.right.right.val == 1


# Test Case 2
#     1             1
#    / \     =>    / \
#   2   3         3   2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()
inverted = solution.invert(root)

assert inverted.val == 1
assert inverted.left.val == 3
assert inverted.right.val == 2


# Test Case 3
#   1               1
root = TreeNode(1)

solution = Solution()
inverted = solution.invert(root)

assert inverted.val == 1
assert inverted.left is None
assert inverted.right is None


# Test Case 4
#   None
root = None

solution = Solution()
inverted = solution.invert(root)

assert inverted is None
