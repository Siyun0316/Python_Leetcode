# Decode String
# Given an encoded string, return it's decoded string.
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid;
# No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and
# that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

import unittest

class Solution(object):
  def decodeString(self, input):
    """
    input: string input
    return: string
    """
    if not input:
        return ""
    i = 0
    _digit = []
    _previous_str = []
    tmp = ''
    count = 0
    while i < len(input):
        if input[i].isdigit():
            count = 0
            while input[i].isdigit():
                count = count*10 + int(input[i])
                i += 1
        elif input[i].isalpha():
            tmp = tmp + input[i]
            i += 1
        elif input[i] == '[':
            _digit.append(count)
            _previous_str.append(tmp)
            tmp = ''
            i +=1
        else:
            rst = _previous_str.pop()
            cnt = _digit.pop()
            tmp = rst + cnt*tmp  # time complexity O(tmp)
            i += 1
    return tmp

# time complexity O(n^2)
# space complexity O(n)


class Test(unittest.TestCase):
    def test_decode(self):
        solution = Solution()

        _input = "3[a]2[bc]"
        expected_result = "aaabcbc"
        self.assertEqual(solution.decodeString(_input), expected_result)

        _input = "3[a2[c]]"
        expected_result = "accaccacc"
        self.assertEqual(solution.decodeString(_input), expected_result)

        _input = "2[abc]3[cd]ef"
        expected_result = "abcabccdcdcdef"
        self.assertEqual(solution.decodeString(_input), expected_result)

        _input = "4[a]4[b]2[cd]2[e]f"
        expected_result = "aaaabbbbcdcdeef"
        self.assertEqual(solution.decodeString(_input), expected_result)

        _input = "abc"
        expected_result = "abc"
        self.assertEqual(solution.decodeString(_input), expected_result)


