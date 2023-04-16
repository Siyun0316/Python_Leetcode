# 440. Binary Tree Path Sum To Target I
# Given a binary tree and a target sum,
# determine if the tree has a root-to-leaf path such that adding up
# all the values along the path equals the given target.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def exist(self, root, target):
        """
        input: TreeNode root, int target
        return: boolean
        """
        return self.helper(root, 0, target)

    def helper(self, root, tmp, target):
        if not root:
            return False
        tmp += root.val
        if not root.left and not root.right:
            return tmp == target
        return self.helper(root.left, tmp, target) or self.helper(root.right, tmp, target)

    def exist2(self, root, target):
        """
        input: TreeNode root, int target
        return: boolean
        """
        if not root:
            return False
        if not root.left and not root.right and target == root.val:
            return True
        return self.exist2(root.left, target - root.val) or self.exist2(root.right, target - root.val)

# time complexity O(n)
# space complexity O(height) O(logn) ~ O(n)


# Test Case 1
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

solution = Solution()
assert solution.exist2(root, 22) == True
assert solution.exist(root, 22) == True


# Test Case 2
#   1
#  / \
# 2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()
assert solution.exist2(root, 4) == True
assert solution.exist(root, 4) == True


# Test Case 3
#   1
root = TreeNode(1)

solution = Solution()
assert solution.exist2(root, 1) == True
assert solution.exist(root, 1) == True


# Test Case 4
#   None
root = None

solution = Solution()
assert solution.exist2(root, 0) == False
assert solution.exist(root, 0) == False


