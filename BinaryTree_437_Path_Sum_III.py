# 437. Path Sum III
# Given the root of a binary tree and an integer targetSum,
# return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (i.e., traveling only from parent nodes to child nodes).

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        self.res = 0
        cache = {0:1}
        self.dfs(root, targetSum, 0, cache)
        return self.res

    def dfs(self, root, target, cur_sum, cache):
        if not root:
            return
        cur_sum += root.val
        # if cur_sum - old_sum == target, res +=1
        old_sum = cur_sum - target
        self.res += cache.get(old_sum, 0)
        cache[cur_sum] = cache.get(cur_sum, 0) +1
        self.dfs(root.left, target, cur_sum, cache)
        self.dfs(root.right, target, cur_sum, cache)
        cache[cur_sum] -= 1

# time complexity O(n)
# space complexity O(n)

# Test Case 1
# tree:
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
assert Solution().pathSum(root, 8) == 3

# Test Case 2
# tree:
#   1
root = TreeNode(1)
assert Solution().pathSum(root, 1) == 1

# Test Case 3
# tree:
#   1
#  / \
# 2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert Solution().pathSum(root, 4) == 1

# Test Case 4
# tree:
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
assert Solution().pathSum(root, 6) == 2

# Test Case 5
assert Solution().pathSum(None, 10) == 0

