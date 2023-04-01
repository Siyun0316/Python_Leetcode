# 2 sum II allow duplicate solution
# Find all pairs of elements in a given array that sum to the pair the given target number.
# Return all the distinct pairs of values.

# The given array has no duplicate value

class Solution(object):
    def twoSum(self,arr,target):
        '''
        :param arr: list[int]
        :param target: int
        :return: list[list[int]]
        '''
        if not arr:
            return [[-1,-1]]
        tmp_hash = dict()
        res = []
        for i in range(len(arr)):
            if arr[i] in tmp_hash:
                res.append([tmp_hash[arr[i]], i])
            else:
                tmp_hash[target - arr[i]] = i
        return res
# time complexity O(n)
# space complexity O(n)
# two pointers method
    def twoSum2(self,nums,target):
        '''
        :param nums list[int]:
        :param target int:
        :return: list[int]
        '''
        if not nums:
            return []
        left,right = 0, len(nums)-1
        nums = sorted (nums) # skip if nums is sorted
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([left,right])
                left +=1
                right -=1
            elif nums[left] + nums[right] > target:
                right -=1
            else:
                left +=1
        return res
# if sorted nums : T O(n) S O(1)
# if unsorted nums : T O(nlogn + n) S O(logn)

test = [1,2,3,4,5,6,7,8]
print(Solution().twoSum(test,8))
print(Solution().twoSum2(test,8))


