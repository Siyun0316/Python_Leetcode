# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper],
# return its missing ranges.
#
# Example:
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        res = []
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == lower +1:
                    res.append(str(lower))
                elif nums[i] == lower:
                    continue
                else:
                    res.append(str(lower)+"->"+str(nums[i]))
            if nums[i]-nums[i-1] == 1:
                continue
            elif nums[i]-nums[i-1] == 2:
                res.append(str(nums[i-1]+1))
            else:
                res.append(str(nums[i-1]+1) + "->" + str(nums[i]-1))
        if nums[-1] == upper-1:
            res.append(str(upper))
        elif nums[-1] < upper:
            res.append(str(nums[-1]+1) +"->" + str(upper))
        return res

# Time: O(N) && Space: O(1)

    def findMissingRanges2(self, nums, lower, upper):
        res = []
        nex = lower
        for i in range(len(nums)):
            if nums[i] < nex:
                continue
            elif nums[i] == nex:
                nex +=1
            else:
                tmp = self.getRange(nex, nums[i]-1)
                res.append (tmp)
                nex = nums[i]+1
        if nex <= upper:
            res.append(self.getRange(nums[-1]+1, upper))

        return res

    def getRange(self, a,b):
        if b==a:
            return str(a)
        return str(a) + "->" + str(b)

# Time: O(N) && Space: O(1)

print(Solution().findMissingRanges([0,2,3,6],0,99))

print(Solution().findMissingRanges2([0,2,3,6],0,99))

print(Solution().findMissingRanges([0,2,3,6,97,99],0,99))

print(Solution().findMissingRanges2([0,2,3,6,97,99],0,99))




