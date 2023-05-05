# Right Shift By N Characters
# Right shift a given string by n characters.
# Assumptions
# The given string is not null.
# n >= 0.
# Examples
# "abc", 4 -> "cab"

import unittest

class Solution(object):
    def rightShift(self, input, n):
        """
        input: string input, int n
        return: string
        """
        if n == 0 or len(input)< 2:
            return input
        k = len(input)
        rem_n = n % k
        res = input
        for i in range(rem_n):
            res = res[-1] + res[:k-1]
        return res

# time complexity O(len(input))
# space complexity O(1)
    def rightShift2(self, input, n):
        """
        input: string input, int n
        return: string
        """
        if n == 0 or len(input)< 2:
            return input
        k = len(input)
        rem_n = n % k
        res = input[k-rem_n:] + input[:k-rem_n]
        return res

# time complexity O(1)
# space complexity O(1)

class Test(unittest.TestCase):
    def test_rightshift(self):

        _input = "abc"
        _num = 4
        _output = "cab"
        self.assertEqual(Solution().rightShift(_input, _num), _output)
        self.assertEqual(Solution().rightShift2(_input, _num), _output)

        _input = "abcdefg"
        _num = 3
        _output = "efgabcd"
        self.assertEqual(Solution().rightShift(_input, _num), _output)
        self.assertEqual(Solution().rightShift2(_input, _num), _output)

        _input = "abcdefg"
        _num = 39
        _output = "defgabc"
        self.assertEqual(Solution().rightShift(_input, _num), _output)
        self.assertEqual(Solution().rightShift2(_input, _num), _output)
