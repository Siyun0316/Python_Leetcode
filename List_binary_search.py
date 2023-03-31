#Classical Binary Search
# Given a target integer T and an integer array A sorted in ascending order,
# find the index i such that A[i] == T or return -1 if there is no such index.

#There can be duplicate elements in the array,
#and you can return any of the indices i such that A[i] == T.

class Solution(object):
    def binarySearch(self,array,target):
        if not array:
            return -1
        l,r = 0,len(array)-1
        while l<=r:
            m = (l+r)//2
            if array[m] == target:
                return m
            elif array[m] > target:
                r = m-1
            else:
                l = m+1
        return -1
# time complexity O(logn)
# space complexity O(1)
test = [1,3,5,7,9,11,13,15,15,15,15]
print(Solution().binarySearch(test,15))
print(Solution().binarySearch(test,12))
print(Solution().binarySearch(test,11))
