# 43. In-order Traversal Of Binary Tree (iterative)
# Implement an iterative, in-order traversal of a given binary tree,
# return the list of keys of each node in the tree as it is in-order traversed.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inOrder(self, root):
        '''
        :param root: TreeNode
        :return: list[int]
        '''
        if not root:
            return []
        tmp = [(root, 1)]
        res = []
        while tmp:
            cur,cnt = tmp.pop()
            if cnt == 1:
                tmp.append((cur,cnt+1))
                if cur.left:
                    tmp.append((cur.left,1))
            elif cnt == 2:
                tmp.append((cur, cnt+1))
                res.append(cur.val)
                if cur.right:
                    tmp.append((cur.right,1))
        return res

# time complexity O(n)
# space complexity O(height)


# Test case 1
#      1
#     / \
#    2   3
# Output: [2, 1, 3]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().inOrder(root))


# Test case 2
#      1
#       \
#        2
# Output: [1, 2]

root = TreeNode(1)
root.right = TreeNode(2)
print(Solution().inOrder(root))


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


# Test case 4
# Output: []

print(Solution().inOrder(None))
