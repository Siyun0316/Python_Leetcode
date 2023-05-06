# Plus One
# Given a non-negative number represented as an array of digits, plus one to the number.
# Input: [2, 5, 9]
# Output: [2, 6, 0]
import unittest

class Solution(object):
    def plus(self, digits):
        """
        input: int[] digits
        return: int[]
        """
        if not digits:
            return [1]
        carry = 1
        k = len(digits) - 1
        while k >= 0 and carry > 0 :
            tmp = (digits[k] + carry)%10
            carry = (digits[k] + carry)//10
            digits[k] = tmp
            k -= 1
        if carry == 1 and k < 0:
            digits = [1] + digits
        return digits

# time complexity O(n)
# space complexity O(1)


class Test(unittest.TestCase):
    def test(self):

        _input = [8,9,9,9]
        _output = [9,0,0,0]
        self.assertEqual(Solution().plus(_input), _output)

        _input = [9, 9, 9, 9]
        _output = [1, 0, 0, 0, 0]
        self.assertEqual(Solution().plus(_input), _output)

        _input = [2, 5, 9]
        _output = [2, 6, 0]
        self.assertEqual(Solution().plus(_input), _output)



