# Last Occurrence
class Solution(object):
    def lastOccurrence(self,array,target):
        '''
        :param array list[int]:
        :param target int:
        :return int:
        '''
        if not array:
            return -1
        l,r = 0, len(array)-1
        while l < r-1:
            m = (l+r)//2
            if array[m] == target:
                l = m
            elif array[m] > target:
                r = m-1
            else:
                l = m+1
        if array[r] == target:
            return r
        if array[l] == target:
            return l
        return -1

# time complexity O(logn)
# space complexity O(1)

#test
test = [1,3,5,7,9,11,11,11,13,15,15,15,15]
print(Solution().lastOccurrence(test,15))
print(Solution().lastOccurrence(test,12))
print(Solution().lastOccurrence(test,11))
print(Solution().lastOccurrence(test,13))
