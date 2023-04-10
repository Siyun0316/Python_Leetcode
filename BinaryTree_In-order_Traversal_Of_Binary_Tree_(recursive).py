# 654. In-order Traversal Of Binary Tree (recursive)
# Implement a recursive, in-order traversal of a given binary tree,
# return the list of keys of each node in the tree as it is in-order traversed.
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def inOrder(self,root):
        """
        input: TreeNode root
        return: Integer[]
        """
        res = []
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if not root:
            return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)
        return

    def inOrder2(self,root):
        """
        input: TreeNode root
        return: Integer[]
        """
        if not root:
            return []
        res = []
        res += self.inOrder2(root.left)
        res.append(root.val)
        res += self.inOrder2(root.right)
        return res

# time complexity O(n)
# space complexity O(n)

# Test case 1
#      1
#     / \
#    2   3
# Output: [2, 1, 3]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().inOrder(root))
print(Solution().inOrder2(root))

# Test case 2
#      1
#       \
#        2
# Output: [1, 2]

root = TreeNode(1)
root.right = TreeNode(2)
print(Solution().inOrder(root))
print(Solution().inOrder2(root))

# Test case 3
#      1
#     / \
#    2   3
#       / \
#      4   5
# Output: [2, 1, 4, 3, 5]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(Solution().inOrder(root))
print(Solution().inOrder2(root))

# Test case 4
# Output: []

print(Solution().inOrder(None))
print(Solution().inOrder2(None))
