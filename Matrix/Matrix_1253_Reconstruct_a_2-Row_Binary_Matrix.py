# 1253. Reconstruct a 2-Row Binary Matrix

import collections


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list[int]) -> list[list[int]]:
        if upper + lower != sum(colsum):
            return  []
        s_dict = collections.Counter(colsum)
        if s_dict.get(2,0) > min(upper, lower):
            return []
        res = [[],[]]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                res[0].append(1)
                res[1].append(1)
            elif colsum[i] == 0:
                res[0].append(0)
                res[1].append(0)
            else:
                if upper > s_dict.get(2,0):
                    res[0].append(1)
                    res[1].append(0)
                    upper -=1
                else:
                    res[1].append(1)
                    res[0].append(0)
        return res
# time complexity O(n)
# space complexity O(1)

print(Solution().reconstructMatrix(2,1,[1,1,1]))

print(Solution().reconstructMatrix(2,3,[2,2,1,1]))

print(Solution().reconstructMatrix(5,5,[2,1,2,0,1,0,1,2,0,1]))