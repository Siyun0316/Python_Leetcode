#Smallest Range Covering Elements from K Lists
#You have k lists of sorted integers in non-decreasing order.
#Find the smallest range that includes at least one number from each of the k lists.
#We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

import heapq
class Solution(object):
    def findSmallestRange(self,arrs):
        '''
        :param arrs list[list[int]]:
        :return list[int]:
        '''
        res = [float('-inf'),float('inf')]
        max_tmp = float('-inf')
        min_h = []
        for i in range(len(arrs)):
            if len(arrs)>0:
                min_h.append((arrs[i][0],i,0))
                max_tmp = max(max_tmp, arrs[i][0])
        heapq.heapify(min_h)
        while len(min_h)== len(arrs):
            min_tmp,row,col = heapq.heappop(min_h)
            if res[1]-res[0]>max_tmp-min_tmp:
                res = [min_tmp,max_tmp]
            if len(arrs[row])>col+1:
                heapq.heappush(min_h,(arrs[row][col+1],row, col+1))
                max_tmp = max(max_tmp,arrs[row][col+1])
        return res
# time complexity O(nlogk)
# space complexity O(k)

test1 = [1,2,3,4,5,6,7]
test2 = [4,5,6,7,9]
test3 = [2,3,4,5,6,9]

print(Solution().findSmallestRange([test1,test2,test3]))
print(Solution().findSmallestRange([test1,test3]))