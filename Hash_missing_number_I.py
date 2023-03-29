# Missing number I
#Given an integer array of size N - 1, containing all the numbers from 1 to N except one,
# find the missing number.
class Solution(object):
    def missingNum(self,array):
        '''
        :input array:
        :return int:
        '''
        set_a = set(array)
        N = len(array)+1
        for i in range(1,N+1):
            if i not in set_a:
                return i
        return -1
# time complexity O(n)
# space complexity O(n)
    def missingNum2(self,array):
        '''
        :param array:
        :return int:
        '''
        N = len(array)+1
        return N*(N+1)//2 - sum(array)
# time complexity O(n)
# space complexity O(1)

#test

array1 = [1,2,3,4,6]
array2 = [1,2,3,4,5]
array3 = [2,3,4,5,6]
print (Solution().missingNum(array1))
print (Solution().missingNum(array2))
print (Solution().missingNum(array3))

print (Solution().missingNum2(array1))
print (Solution().missingNum2(array2))
print (Solution().missingNum2(array3))
