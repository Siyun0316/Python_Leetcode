# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        self.dfs(nums, 0, res)
        return sorted(res)

    def dfs(self, nums, indx, res):
        if indx == len(nums) - 1:
            res.append(nums[:])
            return
        for i in range(indx, len(nums)):
            nums[i], nums[indx] = nums[indx], nums[i]
            self.dfs(nums, indx + 1, res)
            nums[i], nums[indx] = nums[indx], nums[i]
        return

# time complexity O(n*n!)
# space complexity O(n)

s = Solution()

assert s.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
assert s.permute([0,1]) == [[0,1],[1,0]]
assert s.permute([1]) == [[1]]
