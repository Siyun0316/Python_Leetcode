# Binary Tree Path Sum To Target I
# output all the path

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findPath(self, root, target):
        """
        :param root: TreeNode
        :param target: int
        :return: list[list[int]]
        """
        if not root:
            return []
        res = []
        self.helper(root, target, [], res)
        return res

    def helper(self, root, target, path, paths):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and target == root.val:
            paths.append(path)
        self.helper(root.left, target-root.val, path.copy(), paths)
        self.helper(root.right, target-root.val, path.copy(), paths)
        return

    def findPath2(self, root, target):
        if not root:
            return []

        stack = [(root, root.val, [root.val])]
        res = []

        while stack:
            cur, total, path = stack.pop(0)
            if not cur.left and not cur.right and total == target:
                res.append(path)
            if cur.left:
                stack.append((cur.left, total+cur.left.val, path + [cur.left.val]))
            if cur.right:
                stack.append((cur.right, total+cur.right.val, path + [cur.right.val]))
        return res

    def findPath3(self, root, target):
        if not root:
            return []
        res = []

        def dfs(root, target, path):
            if not root:
                return
            if not root.left and not root.right and root.val == target:
                res.append(path + [root.val])
                return
            dfs(root.left, target-root.val, path+[root.val])
            dfs(root.right, target- root.val, path+[root.val])
            return

        dfs(root, target, [])
        return res




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
assert solution.findPath(root, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
#print (Solution().findPath2(root,22))
#assert solution.findPath2(root, 22) == [[5, 8, 4, 5],[5, 4, 11, 2]]
assert solution.findPath2(root, 22) == [[5, 4, 11, 2],[5, 8, 4, 5]]
assert solution.findPath3(root, 22) == [[5, 4, 11, 2],[5, 8, 4, 5]]


# Test Case 2
#   1
#  / \
# 2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()
assert solution.findPath(root, 3) == [[1, 2]]
assert solution.findPath2(root, 3) == [[1, 2]]
assert solution.findPath3(root, 3) == [[1, 2]]


# Test Case 3
#   1
root = TreeNode(1)

solution = Solution()
assert solution.findPath(root, 1) == [[1]]
assert solution.findPath2(root, 1) == [[1]]
assert solution.findPath3(root, 1) == [[1]]


# Test Case 4
#   None
root = None

solution = Solution()
assert solution.findPath(root, 0) == []
assert solution.findPath2(root, 0) == []
assert solution.findPath3(root, 0) == []
