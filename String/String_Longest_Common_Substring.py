# Longest Common Substring
# Find the longest common substring of two given strings.
# Assumptions
# The two given strings are not null
# Examples
# S = “abcde”, T = “cdf”, the longest common substring of S and T is “cd”
import unittest


class Solution(object):
    def longestCommon(self, source, target):
        """
        input: string source, string target
        return: string
        """
        if not source or not target:
            return
        _matrix = [0] * (len(source) + 1)
        for i in range(len(_matrix)):
            _matrix[i] = [0] * (len(target) + 1)
        _max_count = 0
        res = None
        for i in range(len(source)+1):
            for j in range(len(target)+1):
                if i == 0 or j ==0:
                    _matrix[i][j] = 0
                elif source[i-1] == target[j-1]:
                    _matrix[i][j] = _matrix[i-1][j-1] + 1
                    if _max_count < _matrix[i][j]:
                        _max_count = _matrix[i][j]
                        res = source[i-_max_count:i]
                else:
                    _matrix[i][j] = 0
        return res

# time complexity O(mn)
# space complexity O(mn)

class Test(unittest.TestCase):
    def test_longestP(self):

        # Test case 1
        source = "abcdefg"
        target = "def"
        expected_output = "def"
        self.assertEqual(Solution().longestCommon(source,target),expected_output)

        # Test case 2
        source = "abbabcb"
        target = "abc"
        expected_output = "abc"
        self.assertEqual(Solution().longestCommon(source,target),expected_output)

        # Test case 3
        source = "abcd"
        target = "xyz"
        expected_output = None
        self.assertEqual(Solution().longestCommon(source,target),expected_output)

        # Test case 4
        source = ""
        target = "def"
        expected_output = None
        self.assertEqual(Solution().longestCommon(source,target),expected_output)

        # Test case 5
        source = "abbcdefghijjjklmnopqrs"
        target = "jklm"
        expected_output = "jklm"
        self.assertEqual(Solution().longestCommon(source,target),expected_output)
