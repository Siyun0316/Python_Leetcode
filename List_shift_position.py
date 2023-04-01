# 23. Shift Position
# Given an integer array A, A is sorted in ascending order first then shifted by
# an arbitrary number of positions, For Example, A = {3, 4, 5, 1, 2}
# (shifted left by 2 positions). Find the index of the smallest number.
# Assumptions
# There are no duplicate elements in the array
class Solution(object):
    def shiftPosition(self,arr):
        '''
        :param arr: list[int]
        :return: int
        '''
        if len(arr) == 0:
            return -1
        left, right = 0, len(arr)-1
        while left < right -1:
            mid = (left + right)//2
            if arr[right] < arr[mid]:
                left = mid + 1
            else:
                right = mid

        if arr[left]<arr[right]:
            return left
        else:
            return right
#time complexity O(logn)
#space complexity O(1)

test1 = [1,2,3,4,5,6]
test2 = [3,4,5,1,2]
test3 = [2,1]

print(Solution().shiftPosition(test1))
print(Solution().shiftPosition(test2))
print(Solution().shiftPosition(test3))


