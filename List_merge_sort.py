# 9. Merge Sort
# Given an array of integers, sort the elements in the array in ascending order.
# The merge sort algorithm should be used to solve this problem.

class Solution(object):
    def mergeSort(self,array):
        '''
        :param array:  list[int]
        :return:
        '''
        if len(array)<2:
            return array
        m = len(array)//2
        l_arr = self.mergeSort(array[:m])
        r_arr = self.mergeSort(array[m:])
        return self.merge(l_arr,r_arr)

    def merge(self,arr1,arr2):
        '''
        :param arr1: list[int]
        :param arr2: list[int]
        :return: list[int]
        '''
        i,j = 0,0
        res = []
        while i<len(arr1) or j<len(arr2):
            if i >= len(arr1):
                res = res + arr2[j:]
                return res
            if j >= len(arr2):
                res = res + arr1[i:]
                return res
            if arr1[i]< arr2[j]:
                res.append(arr1[i])
                i +=1
            else:
                res.append(arr2[j])
                j +=1
        return res

# time complexity O(nlogn)
# space complexity O(n)

test1 = [1,2,3,4,5,1,2,3,4,3,2,5,6,7,8,9]
test2 = []
test3 = [8,7,6,4,2,1,1,3,4,5]

print(Solution().mergeSort(test1))
print(Solution().mergeSort(test2))
print(Solution().mergeSort(test3))

