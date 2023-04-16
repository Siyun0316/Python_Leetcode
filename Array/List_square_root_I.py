# 161. Square Root I
# Given an integer number n, find its integer square root.
# Assumption:
# n is guaranteed to be >= 0.

class Solution(object):
    def sqrt(self,x):
        '''
        :param x: int
        :return: int
        '''
        if x <0:
            return -1
        if x ==0:
            return 0
        l,r = 1,x
        while True:
            m = (l+r)//2
            if m*m <= x and (m+1)*(m+1)>x  :
                return m
            elif m*m > x:
                r = m-1
            else:
                l = m +1

# time complexity O(logn)
# space complexity O(1)

print(Solution().sqrt(8))
print(Solution().sqrt(9))
print(Solution().sqrt(10))
print(Solution().sqrt(11))