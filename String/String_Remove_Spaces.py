# Remove Spaces
# Given a string, remove all leading/trailing/duplicated empty spaces.
# Assumptions:
# The given string is not null.
# Examples:
# “  a” --> “a”
# “   I     love MTV ” --> “I love MTV”

import unittest

class Solution(object):
  def removeSpaces(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if not input:
        return input
    res = ''
    i = 0
    while i < len(input):
        if input[i] == ' ' and (not res or i+1 == len(input) or (i+1 < len(input) and input[i+1] == ' ')):
            i += 1
        else:
            res = res + input[i]
            i += 1
    return res

# time complexity O(n)
# space complexity O(1)

class Test(unittest.TestCase):
    def test_remove(self):

        _input = "   2223   4124  3  5    "
        _output = "2223 4124 3 5"
        self.assertEqual(Solution().removeSpaces(_input), _output)

        _input = "rwerfw"
        _output = "rwerfw"
        self.assertEqual(Solution().removeSpaces(_input), _output)

        _input = "   rwerfw    "
        _output = "rwerfw"
        self.assertEqual(Solution().removeSpaces(_input), _output)

