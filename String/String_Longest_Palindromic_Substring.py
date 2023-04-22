# Longest Palindromic Substring
# Given a string S, find the longest palindromic substring in S.
# Assumptions
# There exists one unique longest palindromic substring.
# The input S is not null.
# Examples
# Input:     "abbc"
# Output:  "bb"
# Input:     "abcbcbd"
# Output:  "bcbcb"
import unittest
import unittest

class Solution(object):
    def longestPalindrome(self, input):
        """
        input: string input
        return: string
        """
        if len(input) < 2:
            return input
        start, end = 0, 0
        for i in range(len(input)):
            odd_center = self.expandCenter(input, i, i)
            even_center = self.expandCenter(input, i, i+1)
            length = max(odd_center, even_center)

            if length > end - start + 1:
                start = i - (length-1)//2
                end = i + length//2
        return input[start:end+1]

    def expandCenter(self, inp, l, r):
        while l >= 0 and r < len(inp) and inp[l] == inp[r]:
            l -= 1
            r += 1
        return r - l -1

# time complexity O(N^2)
# space complexity O(1)

class Test(unittest.TestCase):
    def test_longestP(self):
        _input = "abbc"
        _output = "bb"
        self.assertEqual(Solution().longestPalindrome(_input), _output)

        _input = "abcbcbd"
        _output = "bcbcb"
        self.assertEqual(Solution().longestPalindrome(_input), _output)

        _input = "bcbccaacdca"
        _output = "acdca"
        self.assertEqual(Solution().longestPalindrome(_input), _output)


