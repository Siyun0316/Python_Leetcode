# Post-order Traversal Of Binary Tree (iterative)
# Implement an iterative, post-order traversal of a given binary tree,
# return the list of keys of each node in the tree as it is post-order traversed.

class TreeNode(object):
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postOrder(self, root):
        """
        input: TreeNode root
        return: Integer[]
        """
        if not root:
            return []
        tmp = [(root,1)]
        res = []
        while tmp:
            cur, cnt = tmp.pop()
            if cnt==1:
                tmp.append((cur,2))
                if cur.left:
                    tmp.append((cur.left,1))
            elif cnt==2:
                tmp.append((cur,3))
                if cur.right:
                    tmp.append((cur.right,1))
            else:
                res.append(cur.val)
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