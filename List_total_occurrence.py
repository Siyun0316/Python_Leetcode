# 24. Total Occurrence
# Given a target integer T and an integer array A sorted in ascending order,
# find the total number of occurrences of T in A.

class Solution(object):
    def totalOccurrence(self,arr,target):
        if not arr:
            return -1
        first = self.firstOccurrence(arr,target)
        last = self.lastOccurrence(arr,target)
        return last-first +1 if first != -1 else -1

    def firstOccurrence(self,arr,target):
        if arr[-1] < target or arr[0] > target:
            return -1
        left, right = 0, len(arr)-1
        while left< right -1:
            mid = (left+right)//2
            if arr[mid]>= target:
                right = mid
            else:
                left = mid + 1
        if arr[right] == target:
            return right
        elif arr[left] == target:
            return left
        else:
            return -1
    def lastOccurrence(self,arr,target):
        if arr[-1] < target or arr[0] > target:
            return -1
        left,right = 0, len(arr)-1
        while left<right-1:
            mid = (left +right)//2
            if arr[mid] <= target:
                left = mid
            else:
                right = mid -1
        if arr[right] == target:
            return right
        elif arr[left] == target:
            return left
        else:
            return -1
# time complexity O(logn)
# space complexity O(1)
test1 = [1,1,1,1,1,1,2,3,3,3,3,4,4,4,4,5,6,7,8,9,10]
test2 = [2,3,5,6,7,8,9,9,9,9,9,9]
print(Solution().totalOccurrence(test1,2))
print(Solution().totalOccurrence(test1,3))
print(Solution().totalOccurrence(test2,4))
print(Solution().totalOccurrence(test2,9))
print(Solution().totalOccurrence(test1,12))

