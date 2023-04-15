# Reverse String
# Reverse a given string.
# Assumptions
# The given string is not null.

class Solution(object):
    def reverse(self, input):
        '''
        :param input: string
        :return: string
        '''
        if not input or len(input)<2:
            return input
        return ''.join(list(input)[::-1])

# time complexity O(n)
# space complexity O(n)

    def reverse2(self, input):
        '''
        :param input: string
        :return: string
        '''
        if not input or len(input)<2:
            return input
        res = ""
        x = len(input) -1
        while x >= 0:
            res = res + input[x]
            x -=1
        return res

# time complexity O(n)
# spcae complexity O(1)



import unittest
class TestReverse(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()

        # Test case 1
        input_str = "hello"
        expected_output = "olleh"
        self.assertEqual(solution.reverse(input_str), expected_output)
        self.assertEqual(solution.reverse2(input_str), expected_output)

        # Test case 2
        input_str = "abcd"
        expected_output = "dcba"
        self.assertEqual(solution.reverse(input_str), expected_output)
        self.assertEqual(solution.reverse2(input_str), expected_output)

        # Test case 3
        input_str = "a"
        expected_output = "a"
        self.assertEqual(solution.reverse(input_str), expected_output)
        self.assertEqual(solution.reverse2(input_str), expected_output)

        # Test case 4
        input_str = ""
        expected_output = ""
        self.assertEqual(solution.reverse(input_str), expected_output)
        self.assertEqual(solution.reverse2(input_str), expected_output)