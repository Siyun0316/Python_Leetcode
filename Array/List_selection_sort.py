# 4. Selection Sort
# Given an array of integers, sort the elements in the array in ascending order.
# The selection sort algorithm should be used to solve this problem.

class Solution(object):
    def selectionSort(self,array):
        '''
        :param array: list[int]
        :return: list[int]
        '''
        if len(array) < 2:
            return array
        for i in range(len(array)):
            cur_min = array[i]
            cur_idx = i
            for j in range(i+1,len(array)):
                if array[j] < cur_min:
                    cur_min = array[j]
                    cur_idx = j
            array[i],array[cur_idx] = array[cur_idx],array[i]
        return array

# time complexity O(n^2)
# space complexity O(1)

print(Solution().selectionSort([2,3,1,4,5,1,2,3,4]))
print(Solution().selectionSort([2,3,1,4,5,6,5,3,7,8,9]))
