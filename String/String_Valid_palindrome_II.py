# Valid palindrome II
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
import unittest

class Solution(object):
    def validPalindrome(self, input):
        """
        input: string input
        return: boolean
        """
        if not input or len(input) < 3:
            return True
        l, r = 0, len(input) - 1
        while l < r :
            if input[l] != input[r] :
                return self.helper(input, l+1, r) or self.helper(input, l, r-1)
            else:
                l += 1
                r -= 1
        return True

    def helper(self, inp, l, r):
        while l < r:
            if inp[l] != inp[r]:
                return False
            l += 1
            r -= 1
        return True

# time complexity O(n)
# space complexity O(1)

class Test(unittest.TestCase):
    def test(self):


        _input = "oklvojceguiuooqfsvlappalvsfqoouiuigecjovlko"
        _output = True
        self.assertEqual(Solution().validPalindrome(_input), _output)

        _input = "abca"
        _output = True
        self.assertEqual(Solution().validPalindrome(_input), _output)

        _input = "veojdxwdxiaygjcevivpmuuoflpxgsoajlfyzexfhaptxkngsxabjxpipusqbbqsupipxjbaxsgnkxtpahfxezyfljaosgxplfouumpvivecjgykaixdwxdjoev"
        _output = True
        self.assertEqual(Solution().validPalindrome(_input), _output)



