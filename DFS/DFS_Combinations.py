# Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# E.g.    Input: n = 4, k = 2
#     Output: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

class Solution(object):
    def combine(self, n, k):
        """
        input: int n, int k
        return: int[][]
        """
        res = []
        tmp = []
        def dfs(tmp, idx):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            for i in range(idx, n+1):
                tmp.append(i)
                dfs(tmp, idx+1)
                tmp.pop()
            return
        dfs(tmp,1)
        return res
# time complexity O(n*(n-1)*(n-2)...(n-k))
# space complexity O(k)

def test_combine():
    s = Solution()
    assert s.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combine(3, 3) == [[1, 2, 3]]
    assert s.combine(1, 1) == [[1]]
    assert s.combine(5, 0) == [[]]
