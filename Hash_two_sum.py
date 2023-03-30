#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        '''
        :param nums list[int]:
        :param target int:
        :return:
        '''
        if not nums:
            return []
        tmp_dic = {}
        for i in range(len(nums)):
            if nums[i] in tmp_dic:
                return [tmp_dic[nums[i]],i]
            else:
                tmp_dic[target-nums[i]] = i
        return []

# time complexity O(n)
# space complexity O(n)

test_l = [ 1,2,3,5,6,7,8]
target = 5
print (Solution().twoSum(test_l,target))





