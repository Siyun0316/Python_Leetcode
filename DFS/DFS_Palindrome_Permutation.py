# Palindrome Permutation
# Given a string, determine if a permutation of the string could form a palindrome.
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, input):
        """
        input: string input
        return: boolean
        """
        # write your solution here
        if len(input) < 2:
            return True
        odd = 0
        _count = Counter(input)
        for key, val in _count.items():
            if val%2 == 1:
                odd += 1
        return odd < 2

# time complexity O(n)
# space complexity O(n)

def test_canPermutePalindrome():
    s1 = "aab"
    assert Solution().canPermutePalindrome(s1) == True

    s2 = "code"
    assert Solution().canPermutePalindrome(s2) == False

    s3 = "a"
    assert Solution().canPermutePalindrome(s3) == True

    s4 = ""
    assert Solution().canPermutePalindrome(s4) == True

    s5 = "racecar"
    assert Solution().canPermutePalindrome(s5) == True

    s6 = "abcabc"
    assert Solution().canPermutePalindrome(s6) == False
