# 656. Post-order Traversal Of Binary Tree (recursive)
# Implement a recursive, post-order traversal of a given binary tree,
# return the list of keys of each node in the tree as it is post-order traversed.

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def postOrder(self,root):
        if not root:
            return []
        res = []
        res += self.postOrder(root.right)
        res.append(root.val)
        res += self.postOrder(root.left)
        return res

# time complexity O(n)
# space complexity O(logn) ~ O(n)

# Test case 1
#      1
#     / \
#    2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().postOrder(root))


# Test case 2
#      1
#       \
#        2

root = TreeNode(1)
root.right = TreeNode(2)
print(Solution().postOrder(root))


# Test case 3
#      1
#     / \
#    2   3
#       / \
#      4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(Solution().postOrder(root))


# Test case 4
# Output: []

print(Solution().postOrder(None))
