# Closest in sorted array

class Solution(object):
    def closest(self,array,target):
        '''
        :param array list[int]:
        :param target int:
        :return int:
        '''
        if len(array)<1:
            return -1
        l,r = 0, len(array)-1
        while l < r-1:
            m = (l+r)//2
            if array[m] == target:
                return m
            elif array[m] > target:
                r = m
            else:
                l = m
        return l if abs(array[l]-target) <= abs(array[r]-target) else r

# time complexity O(logn)
# space complexity O(1)

#test
test = [1,3,5,7,9,11,11,11,13,15,15,15,15]
print(Solution().closest(test,15))
print(Solution().closest(test,12))
print(Solution().closest(test,11))
print(Solution().closest(test,13))
