'''
Given an array A of integers andGiven an array A of integers and integer K,
return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.

Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15. integer K,
return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.

'''

class Solution(object):
    def twoSumLessK(self, arr, k):
        if len(arr)< 2 :
            return -1
        arr.sort()
        ans = -1
        st = 0
        end = len(arr)-1
        while st < end:
            if arr[st] + arr[end] >= k:
                end -= 1
            else:
                ans = max(ans, arr[st] + arr[end])
                st += 1
        return ans

print (Solution().twoSumLessK([1,23,4,5,3,7], 12))

print (Solution().twoSumLessK([1,23,4,5,3,7], 1))

print (Solution().twoSumLessK([1,23,4,5,3,7], 80))




