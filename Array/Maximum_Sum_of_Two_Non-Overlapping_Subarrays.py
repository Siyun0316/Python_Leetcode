'''
Given an integer array nums and two integers firstLen and secondLen,
return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen,
but they have to be non-overlapping.

A subarray is a contiguous part of an array.
'''

class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen) -> int:
        if len(nums) == firstLen + secondLen:
            return sum(nums)
        ans1 = self.helper(nums, firstLen, secondLen)
        ans2 = self.helper(nums, secondLen, firstLen)
        return max(ans1, ans2)

    def helper(self, nums, L,R):
        ans = sum(nums[:L+R])
        max_L = sum(nums[:L])
        ans_L = sum(nums[:L])
        ans_R = sum(nums[L:L+R])
        for i in range(L+R, len(nums)):
            ans_R = ans_R + nums[i] - nums[i-R]
            ans_L = ans_L + nums[i-R] - nums[i-L-R]
            max_L = max(max_L, ans_L)
            ans = max(ans, max_L + ans_R)
        return ans

# time complexity O(n)
# space complexity O(1)

print(Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2))

print(Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3,2))

print(Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))