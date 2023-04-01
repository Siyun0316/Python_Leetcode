# Search In Unknown Sized Sorted Array
# Given an integer dictionary A of unknown size, where the numbers in the dictionary are sorted in ascending order,
# determine if a given target integer T is in the dictionary.
# Return the index of T in A, return -1 if T is not in A.
# dictionary A is not null
# dictionary.get(i) will return null(Java)/INT_MIN(C++)/None(Python) if index i is out of bounds
class Solution(object):
    def searchUnknownArray(self,dic,target):
        '''
        :param dic: dic{}
        :param target: int
        :return: int
        '''
        if not dic or dic.get(0) > target:
            return -1
        far = 1
        while dic.get(far) and dic.get(far) < target:
            far = far*2
        left, right = far//2, far
        while left <=right:
            mid = (left + right)//2
            # check whether mid index is valid
            if not dic.get(mid) or dic.get(mid) > target:
                right = mid - 1
            elif dic.get(mid) < target:
                left = mid + 1
            else:
                return mid
        return -1

# time complexity O(logn)
# space complexity O(1)

test = {0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:12,12:13,13:14,14:15,15:16}
print(Solution().searchUnknownArray(test,11))
print(Solution().searchUnknownArray(test,12))
print(Solution().searchUnknownArray(test,15))
print(Solution().searchUnknownArray(test,19))
