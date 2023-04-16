# Valid palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters('0'-'9','a'-'z','A'-'Z') and ignoring cases.
# For example,
# "an apple, :) elp pana#" is a palindrome.
# "dia monds dn dia" is not a palindrome.

class Solution(object):
  def valid(self, input):
    """
    input: string input
    return: boolean
    """
    if len(input)<2:
        return True
    st = 0
    end = len(input) - 1
    while st < end:
        if not input[st].isalnum():
            st +=1
        elif not input[end].isalnum():
            end -=1
        else:
            if input[st].lower() != input[end].lower():
                return False
            else:
                st +=1
                end -=1
    return True

# time complexity O(n)
# space complexity O(1)

import unittest
class Test(unittest.TestCase):
    def test_valid(self):
        solution = Solution()

        _input = "an apple, :) elp pana#"
        expected_result = True
        self.assertEqual(solution.valid(_input),expected_result)

        _input = "dia monds dn dia"
        expected_result = False
        self.assertEqual(solution.valid(_input), expected_result)
