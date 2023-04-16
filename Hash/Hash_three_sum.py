# 3 Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self,nums):
        '''
        :param nums: list[int]
        :return: list[int]
        '''
        if not nums or len(nums)<3:
            return []
        res_s = set()
        res_lst = []
        for i,v in enumerate(nums[:-2]):
            if i>0 and v == nums[i-1]:
                continue
            tmp_dict = {}
            for x in nums[i+1:]:
                if x in tmp_dict:
                    if (v,x,-v-x) not in res_s:
                        res_lst.append([v,x,-v-x])
                    res_s.add((v,x,-v-x))
                else:
                    tmp_dict[-v-x] =1
        return res_lst

# time complexity O(n^2)
# space complexity O(n)

    def threeSum2(self,nums):
        '''
        :param nums: list[int]
        :return: list[int]
        '''
        if not nums or len(nums)<3:
            return []
        res_s = set()
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            tmp_dict = {}
            for j in range(i+1,len(nums)):
                if nums[j] in tmp_dict:
                    res_s.add((nums[i], nums[j], -nums[i] - nums[j]))
                else:
                    tmp_dict[-nums[i]-nums[j]] = 1
        return list(map(list,res_s))

# time complexity O(n^2)
# space complexity O(n)

    def threeSum3(self,nums):
        '''
        :param nums: list[int]
        :return: list[int]
        '''
        if not nums or len(nums)<3:
            return []
        res_s = []
        nums.sort()
        for i,v in enumerate(nums[:-2]):
            if i>0 and v == nums[i-1]:
                continue
            left,right = i+1, len(nums)-1
            while left < right:
                cmb = v + nums[left] + nums[right]
                if cmb == 0:
                    res_s.append([v, nums[left],nums[right]])
                    while left< right and nums[left] == nums[left+1]:
                        left +=1
                    while left< right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
                elif cmb >0:
                    right -=1
                else:
                    left +=1
        return res_s

# time complexity O(n^2)
# space complexity O(n)
    def threeSum4(self,nums):
        '''
        :param nums: list[int]
        :return: list[int]
        '''
        if not nums or len(nums)<3:
            return []
        p,z,n = [],[],[]
        res = set()
        for x in nums:
            if x >0 :
                p.append(x)
            elif x ==0:
                z.append(x)
            else:
                n.append(x)
        N, P = set(n), set(p)
        if z:
            for x in N:
                if -x in P:
                    res.add((x,0,-x))
            if len(z) >=3:
                res.add((0, 0, 0))
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                if -n[i]-n[j] in P:
                    res.add((n[i],n[j],-n[i]-n[j]))
        for i in range(len(p)-1):
            for j in range(i+1, len(p)):
                if -p[i]-p[j] in N:
                    res.add((p[i],p[j],-p[i]-p[j]))
        return list(map(list,res))

# time complexity O(n^2)
# space complexity O(n)

test = [-1,-2,-2,-3,-4,0,0,0,1,2,3,4]
test2 = [-1,-2,-3,-4,0,0,0,1,2,3,4,4,4,4,5]
print (Solution().threeSum(test))
print (Solution().threeSum2(test))
print (Solution().threeSum3(test))
print (Solution().threeSum4(test))

print (Solution().threeSum(test2))
print (Solution().threeSum2(test2))
print (Solution().threeSum3(test2))
print (Solution().threeSum4(test2))





