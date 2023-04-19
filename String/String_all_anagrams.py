# All Anagrams
# Find all occurrence of anagrams of a given string s in a given string l. Return the list of starting indices.
# Assumptions
# sh is not null or empty.
# lo is not null.
# Example
# l = "abcbac", s = "ab",
# return [0, 3] since the substring with length 2 starting from index 0/3 are all anagrams of "ab" ("ab", "ba").
from collections import defaultdict
from unittest import TestCase


class Solution(object):
    def allAnagrams(self, sh, lo):
        """
        input: string sh, string lo
        return: Integer[]
        """
        # sliding window with fixed window size, one pointer
        if len(lo) < len(sh):
            return []
        distinct_char_sh = 0
        dict_sh = defaultdict()
        for x in sh:
            if x not in dict_sh:
                distinct_char_sh += 1
                dict_sh[x] = 1
            else:
                dict_sh[x] += 1
        res = []
        count = 0
        for end in range(len(lo)):
            if lo[end] in dict_sh:
                dict_sh[lo[end]] -= 1
                if dict_sh[lo[end]] == 0:
                    count += 1
            if end >= len(sh) and lo[end - len(sh)] in dict_sh:
                dict_sh[lo[end - len(sh)]] += 1
                if dict_sh[lo[end - len(sh)]] == 1:
                    count -= 1
            if count == distinct_char_sh:
                res.append(end - len(sh) + 1)
        return res

# time complexity O(n)
# space complexity O(m)



    def allAnagrams2(self, sh, lo):
        """
        input: string sh, string lo
        return: Integer[]
        """
        # sliding window with two pointers
        if len(lo) < len(sh):
            return []
        dict_sh = defaultdict()
        for x in sh:
            if x not in dict_sh:
                dict_sh[x] = 1
            else:
                dict_sh[x] += 1
        res = []
        st, end = 0, 0
        while end < len(lo):
            if dict_sh.get(lo[end], 0) > 0:
                dict_sh[lo[end]] -= 1
                end += 1
                if end - st == len(sh):
                    res.append(st)
            elif st == end:
                st += 1
                end += 1
            else:
                dict_sh[lo[st]] += 1
                st += 1
        return res

# time complexity O(n)
# space complexity O(m)



# create a test case class


class TestSolution(TestCase):
    def setUp(self):
        # initialize the solutions
        self.sol = Solution()

    def test_allAnagrams(self):
        # define test cases
        test_cases = [
            ("abc", "cbaebabacd", [0, 6]),
            ("ab", "eidbaooo", [3]),
            ("abcd", "aabbcddcda", [])
        ]
        # test each case
        for sh, lo, expected in test_cases:
            self.assertEqual(self.sol.allAnagrams(sh, lo), expected)

    def test_allAnagrams2(self):
        # define test cases
        test_cases = [
            ("abc", "cbaebabacd", [0, 6]),
            ("ab", "eidbaooo", [3]),
            ("abcd", "aabbcddcda", [])
        ]
        # test each case
        for sh, lo, expected in test_cases:
            self.assertEqual(self.sol.allAnagrams2(sh, lo), expected)
