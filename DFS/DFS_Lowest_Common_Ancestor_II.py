# Lowest Common Ancestor II
# Given two nodes in a binary tree (with parent pointer available), find their lowest common ancestor.
# Assumptions
# There is parent pointer for the nodes in the binary tree
# The given two nodes are not guaranteed to be in the binary tree


class TreeNodeP(object):
    def __init__(self, x, p):
        self.value = x
        self.left = None
        self.right = None
        self.parent = p


class Solution(object):
    def lowestCommonAncestor(self, one, two):
        """
        input: TreeNodeP one, TreeNodeP two
        return: TreeNodeP
        """
        # write your solution here
        if not one or not two:
            return None
        one_h = self.findheight(one)
        two_h = self.findheight(two)
        _short, _short_node = 0, None
        _long, _long_node = 0, None
        if one_h <= two_h:
            _short, _short_node = one_h, one
            _long, _long_node = two_h, two
        else:
            _short, _short_node = two_h, two
            _long, _long_node = one_h, one
        while _short < _long:
            _long_node = _long_node.parent
            _long -= 1
        while _short != 0:
            if _short_node == _long_node:
                return _short_node
            _short_node = _short_node.parent
            _long_node = _long_node.parent
            _short -= 1
        return None

    def findheight(self, node):
        height = 0
        while node:
            height += 1
            node = node.parent
        return height

# time complexity O(n)
# space complexity O(1)

    def lowestCommonAncestor2(self, one, two):
        """
        input: TreeNodeP one, TreeNodeP two
        return: TreeNodeP
        """
        # write your solution here
        if not one or not two:
            return None
        parent_set = set()
        while one:
            parent_set.add(one)
            one = one.parent
        while two:
            if two in parent_set:
                return two
            two = two.parent
        return None

# time complexity O(n)
# space complexity O(n)
