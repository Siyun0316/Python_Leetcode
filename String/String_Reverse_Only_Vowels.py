# Reverse Only Vowels
# Only reverse the vowels('a', 'e', 'i', 'o', 'u') in a given string, the other characters should not be moved or changed.
# Assumptions:
# The given string is not null, and only contains lower case letters.

class Solution(object):
    def reverse(self, input):
        """
        input: string input
        return: string
        """
        if len(input)<2:
            return input
        vowels = {'a', 'e', 'i', 'o', 'u'}
        list_input = list(input)
        st, end = 0, len(input)-1
        while st < end:
            if list_input[st] not in vowels:
                st += 1
            elif list_input[end] not in vowels:
                end -= 1
            else:
                list_input[st], list_input[end] = list_input[end], list_input[st]
                st += 1
                end -= 1
        return ''.join(list_input)

# time complexity O(n)
# spcae complexity O(1)

import unittest

class Test(unittest.TestCase):
    def testReverse(self):
        solution = Solution()

        _input = "abbegi"
        expected_output = "ibbega"
        self.assertEqual(solution.reverse(_input),expected_output)