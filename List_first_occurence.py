# First Occurrence
class Solution(object):
    def firstOccurrence(self,array,target):
        '''
        :param array list[int]:
        :param target int:
        :return:
        '''
        if not array:
            return -1
        l,r = 0, len(array)-1
        while l<r-1:
            m = (l+r)//2
            if array[m]>target:
                r = m-1
            elif array[m] == target:
                r = m
            else:
                l = m+1
        if array[l] == target:
            return l
        elif array[r] == target:
            return r
        else:
            return -1
# time complexity O(logn)
# space complexity O(1)
test = [1,3,5,7,9,11,11,11,13,15,15,15,15]
print(Solution().firstOccurrence(test,15))
print(Solution().firstOccurrence(test,12))
print(Solution().firstOccurrence(test,11))
print(Solution().firstOccurrence(test,13))
