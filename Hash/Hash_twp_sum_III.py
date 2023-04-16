# 2 sum III allow duplicate numbers and solutions
# Find all pairs of elements in a given array that sum to the pair the given target number.
# Return all the distinct pairs of values.
# the order of the values in the pair does not matter
# The given array has duplicate values

from collections import defaultdict
class Solution(object):
    def twoSum(self,arr,target):
        '''
        :param arr: list[list[int]]
        :param target: int
        :return: list[list[int]]
        '''
        if not arr:
            return [[]]
        tmp_dic = defaultdict()
        for x in range(len(arr)):
            if arr[x] not in tmp_dic:
                tmp_dic[arr[x]] = [x]
            else:
                tmp_dic[arr[x]].append(x)
        res = []
        for i in range(len(arr)):
            cur_val = arr[i]
            rem_val = target-arr[i]
            if cur_val in tmp_dic and rem_val in tmp_dic:
                rem_lst = tmp_dic.get(rem_val)
                for j in rem_lst:
                    if j > i:  # avoid i == j or avoid ( i!=j and arr[i] == arr[j] )  output both [i,j] and [j,i]
                        res.append([i,j])
        return res
# time complexity O(n + n^2) worst
# space complexity O(n)

test = [1,2,2,2,2,2,3,4,5]
test2 = [2,2,2]
print (Solution().twoSum(test,4))
print (Solution().twoSum(test2,4))


