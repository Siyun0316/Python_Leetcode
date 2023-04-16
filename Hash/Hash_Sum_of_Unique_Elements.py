# Sum of Unique Elements
# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
import heapq
from collections import Counter
class Solution(object):
    def sumUniqueElements(self,arr):
        '''
        :param arr list[int]:
        :return int:
        '''
        tmp_dic = {}
        res = 0
        for x in arr:
            res += x
            if tmp_dic.get(x,0) ==0:
                tmp_dic[x] =1
            elif tmp_dic[x] ==1:
                tmp_dic[x] +=1
                res -= x*2
            else:
                tmp_dic[x] +=2
                res -=x
        return res

#time complexity O(n)
#space complexity O(n)

    def sumUniqueElements2(self,arr):
        '''
        :param arr list[int]:
        :return int:
        '''
        return sum(k if v ==1 else 0 for k,v in Counter(arr).items())

#time complexity O(n)
#space complexity O(n)

# test
test1 = [1,2,3,4,5,6,1,1,1,1]
test2 = [1,2,3,4,5,6,1,1,2,2,2,2,3,1]

print(Solution().sumUniqueElements(test1))
print(Solution().sumUniqueElements(test2))

print(Solution().sumUniqueElements2(test1))
print(Solution().sumUniqueElements2(test2))