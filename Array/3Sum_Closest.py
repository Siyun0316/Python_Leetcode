# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self,nums, target):
        if len(nums)<3:
            return
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        closest = sum(nums[:3])
        for i in range (len(nums)-2):
            st = i+1
            end = len(nums) -1
            while st < end:
                cur = nums[i] + nums[st] + nums[end]
                if abs(cur - target) < abs(closest - target):
                    closest = cur
                if cur == target:
                    return target
                elif cur > target:
                    end -=1
                else:
                    st +=1
        return closest

print(Solution().threeSumClosest([1,1,2,3,4,-2,3,-2,3,-4],5))

print(Solution().threeSumClosest([1,1,2,3,4,-2,3,-2,3,-4],8))

print(Solution().threeSumClosest([1,1,2,3,4,-2,3,-2,3,-4],-6))



