# First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
# s = "laicode"
# return 0.
# s = "lovelaicode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

from collections import defaultdict
import unittest

class Solution(object):
    def firstUniqChar(self, input):
        """
        input: string input
        return: int
        """
        if len(input) < 2:
            return 0

        tmp_dict = defaultdict(str)
        for x in input:
            tmp_dict[x] = tmp_dict.get(x, 0) +1
        for i,v in enumerate(input):
            if tmp_dict[v] == 1:
                return i
        return -1

# time complexity O(n)
# space complexity O(n)

    def firstUniqChar2(self, input):
        """
        input: string input
        return: int
        """
        if len(input) < 2:
            return 0
        tmp_set = set()
        for i, v in enumerate(input):
            flag = True
            if v in tmp_set:
                flag = False
            tmp_set.add(v)
            for j in range(i+1, len(input)):
                if input[j] == input[i]:
                    flag = False
                    break
            if flag:
                return i
        return -1

# time complexity O(n^2)
# space complexity O(n)

class Test(unittest.TestCase):
    def test_firstUniq(self):
        solution = Solution()

        input = "leetcode"
        output = 0
        self.assertEqual(solution.firstUniqChar(input),output)
        self.assertEqual(solution.firstUniqChar2(input), output)

        input = "loveleetcode"
        output = 2
        self.assertEqual(solution.firstUniqChar(input), output)
        self.assertEqual(solution.firstUniqChar2(input), output)

        input = "abab"
        output = -1
        self.assertEqual(solution.firstUniqChar(input), output)
        self.assertEqual(solution.firstUniqChar2(input), output)

        input = ""
        output = 0
        self.assertEqual(solution.firstUniqChar(input), output)
        self.assertEqual(solution.firstUniqChar2(input), output)