# All Subsets II
# Given a set of characters represented by a String, return a list containing all subsets of the characters.
# Notice that each subset returned will be sorted to remove the sequence.
# Assumptions
# There could be duplicate characters in the original set.


class Solution(object):
    def subSets(self, set):
        """
        input : String set
        return : String[]
        """
        # write your solution here
        nums = list(set)
        nums.sort()
        res = []
        curSet = []
        def dfs(idx):
            res.append(''.join(curSet))
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1] :
                    continue
                curSet.append(nums[i])
                dfs(i+1)
                curSet.pop()
        dfs(0)
        return res

# time complexity O(2^n*n)
# space complexity O(2^n)


def test_subSets():
    s = Solution()

    # Test Case 1
    set1 = "abc"
    expected1 = ["", "a", "ab", "abc", "ac", "b", "bc", "c"]
    assert s.subSets(set1) == expected1

    # Test Case 2
    set2 = "a"
    expected2 = ["", "a"]
    assert s.subSets(set2) == expected2

    # Test Case 3
    set3 = ""
    expected3 = [""]
    assert s.subSets(set3) == expected3

    # Test Case 4
    set4 = "aab"
    expected4 = ["", "a", "aa", "aab", "ab", "b"]
    assert s.subSets(set4) == expected4
