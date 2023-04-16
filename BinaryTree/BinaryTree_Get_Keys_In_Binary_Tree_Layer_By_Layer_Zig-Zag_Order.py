# Get the list of keys in a given binary tree layer by layer in zig-zag order.
# Examples
#
#         5
#
#       /    \
#
#     3        8
#
#   /   \        \
#
#  1     4        11
#
# the result is [5, 3, 8, 11, 4, 1]
#
# Corner Cases
#
# What if the binary tree is null? Return an empty list in this case.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigZag(self, root):
        """
        input: TreeNode root
        return: Integer[]
        """
        if not root:
            return []
        tmp = [root]
        res = []
        flag = True
        while tmp:
            cur_lvl = len(tmp)
            cur_res = []
            for i in range(cur_lvl):
                cur = tmp.pop(0)
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
                cur_res.append(cur.val)
            if flag:
                res = res + cur_res[::-1]
            else:
                res = res + cur_res
            flag = not flag
        return res

# time complexity O(n)
# space complexity O(logn)

# Test Case 1
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
# Expected Output: [1, 2, 3, 6, 5, 4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print(Solution().zigZag(root))

# Test Case 2
#     1
#      \
#       2
#        \
#         3
# Expected Output: [1, 2, 3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print(Solution().zigZag(root))

# Test Case 3
#     1
#    /
#   2
#  /
# 3
# Expected Output: [1, 2, 3]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(Solution().zigZag(root))

# Test Case 4
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6
#       \
#        7
# Expected Output: [1, 2, 3, 6, 5, 4, 7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.right = TreeNode(7)
print(Solution().zigZag(root))




