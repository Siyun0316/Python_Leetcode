# K closest in sorted array
class Solution(object):
    def kClosest(self,array,target,k):
        '''
        :param array list[int]:
        :param target int:
        :return:
        '''
        if len(array) == 1 or k == 0:
            return[]
        closest = self.closest(array,target)
        res = [array[closest]]
        l,r = closest -1, closest+1
        while len(res)<k and (l>=0 or r < len(array)):
            if l>=0 and(r>=len(array) or abs(array[l]-target) <= abs(array[r]-target)):
                res.append(array[l])
                l -=1
            else:
                res.append(array[r])
                r +=1
        return res



    def closest(self,array,target):
        '''
        :param array list[int]:
        :param target int:
        :return int:
        '''
        if len(array)<1:
            return -1
        l,r = 0, len(array)-1
        while l < r-1:
            m = (l+r)//2
            if array[m] == target:
                return m
            elif array[m] > target:
                r = m
            else:
                l = m
        return l if abs(array[l]-target) <= abs(array[r]-target) else r

# time complexity O(logn + k)
# space complexity O(1)

#test
test = [1,3,5,7,9,11,11,11,13,15,15,15,15]
print(Solution().kClosest(test,15,3))
print(Solution().kClosest(test,12,5))
print(Solution().kClosest(test,11,20))
print(Solution().kClosest(test,13,3))
