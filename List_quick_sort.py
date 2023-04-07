# 10. Quick Sort
# Given an array of integers, sort the elements in the array in ascending order.
# The quick sort algorithm should be used to solve this problem.

import random

class Solution(object):
    def quickSort(self,array):
        '''
        :param array: list[int]
        :return: list[int]
        '''
        if len(array)<2:
            return array
        self._sort(array,0,len(array)-1)
        return array

    def partition(self,array,l,r):
        if l >=r:
            return l
        p_indx = random.randint(l,r)
        p_val = array[p_indx]
        array[r],array[p_indx] = array[p_indx],array[r]
        s,e = l,r-1
        while s<=e:
            if array[s]<p_val:
                s +=1
            elif array[e] >= p_val:
                e -=1
            else:
                array[s],array[e] = array[e],array[s]
                s +=1
                e -=1
        array[s],array[r] =array[r],array[s]
        return s

    def _sort(self,array,l,r):
        if l>=r:
            return
        p_idx = self.partition(array,l,r)
        self._sort(array,l,p_idx-1)
        self._sort(array,p_idx+1,r)
        return

# time complexity O(nlogn)
# space complexity O(logn)

test1 = [1,2,3,4,5,1,2,3,4,3,2,5,6,7,8,9]
test2 = []
test3 = [8,7,6,4,2,1,1,3,4,5]

print(Solution().quickSort(test1))
print(Solution().quickSort(test2))
print(Solution().quickSort(test3))

