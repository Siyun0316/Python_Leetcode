# Remove Certain Characters
# Remove given characters in input string, the relative order of other characters should be remained.
# Return the new string after deletion.
# Assumptions
# The given input string is not null.
# The characters to be removed is given by another string, it is guaranteed to be not null.

class Solution(object):
  def remove(self, input, t):
    """
    input: string input, string t
    return: string
    """
    if not input or not t:
        return input
    tmp = set(t)
    res = ""
    for x in input:
        if x not in tmp:
            res = res + x
    return res

# time complexity O(n)
# space complexity O(k) O(1)

import unittest
class Test(unittest.TestCase):
    def test_remove(self):
        solution = Solution()

        _input = "abcd"
        _t = "ab"
        expected_output = "cd"
        self.assertEqual(solution.remove(_input, _t), expected_output)

        # Test case 1
        input_str = "hello world"
        remove_str = "ol"
        expected_output = "he wrd"
        self.assertEqual(solution.remove(input_str, remove_str), expected_output)

        # Test case 2
        input_str = "aabbcc"
        remove_str = "ab"
        expected_output = "cc"
        self.assertEqual(solution.remove(input_str, remove_str), expected_output)

        # Test case 3
        input_str = "aaaa"
        remove_str = "b"
        expected_output = "aaaa"
        self.assertEqual(solution.remove(input_str, remove_str), expected_output)

        # Test case 4
        input_str = "123456789"
        remove_str = "147"
        expected_output = "235689"
        self.assertEqual(solution.remove(input_str, remove_str), expected_output)

