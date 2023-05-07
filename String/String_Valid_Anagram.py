# Valid Anagram
# Given two strings s and t, write a function to determine if t is an anagram of s.
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

from collections import Counter
import unittest

class Solution(object):
    def isAnagram(self, source, target):
        """
        input: string source, string target
        return: boolean
        """
        if len(source) != len(target):
            return False
        tmp = Counter(source)
        for x in target:
            if x not in tmp or tmp[x] == 0:
                return False
            tmp[x] -= 1
        return True

# time complexity O(n)
# space complexity O(n)

class Test(unittest.TestCase):
    def test(self):
        _s = "anagram"
        _t = "nagaram"
        _out = True
        self.assertEqual(Solution().isAnagram(_s, _t), _out)

        _s = "rat"
        _t = "ant"
        _out = False
        self.assertEqual(Solution().isAnagram(_s, _t), _out)


        _s = "abc"
        _t = "cde"
        _out = False
        self.assertEqual(Solution().isAnagram(_s, _t), _out)


