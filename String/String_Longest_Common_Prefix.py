# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

import unittest

class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    input: string[] strs
    return: string
    """
    # write your solution here
    res = ''
    for i in range(len(strs[0])):
      for s in strs:
        if i == len(s) or s[i] != strs[0][i]:
          return res
      res += strs[0][i]
    return res

# time complexity O(m*n)
# space complexity O(1)

  def longestCommonPrefix2(self, strs):
    """
    input: string[] strs
    return: string
    """
    # write your solution here
    strs = sorted(strs)
    for i in range(min(len(strs[0]),len(strs[-1]))):
      if strs[0][i] != strs[-1][i]:
        break
    return strs[0][:i]

# time complexity O(n*logn + m )
# space complexity O(1)

class Test(unittest.TestCase):
  def test(self):

    _inp = ["flower","flow","flight"]
    _out = "fl"
    self.assertEqual(Solution().longestCommonPrefix(_inp), _out)
    self.assertEqual(Solution().longestCommonPrefix2(_inp), _out)

    _inp = ["dog","racecar","car"]
    _out = ""
    self.assertEqual(Solution().longestCommonPrefix(_inp), _out)
    self.assertEqual(Solution().longestCommonPrefix2(_inp), _out)

    