# 11. Rainbow Sort
# Given an array of balls, where the color of the balls can only be Red, Green or Blue,
# sort the balls such that all the Red balls are grouped on the left side,
# all the Green balls are grouped in the middle and all the Blue balls are grouped on the right side.
# (Red is denoted by -1, Green is denoted by 0, and Blue is denoted by 1).

class Solution(object):
    def rainbowSort(self,array):
        '''
        :param array: list[int]
        :return:
        '''
        if len(array) < 2:
            return array
        start, end  = 0,len(array)-1
        i = 0
        # array[:start] -> -1 array[start:end] -> 0 array[end:] -> 1
        while i <= end:
            if array[i] == -1:
                array[i],array[start] = array[start],array[i]
                i += 1
                start += 1
            elif array[i] == 1:
                array[i],array[end] = array[end],array[i]
                end -= 1
            else:
                i +=1
        return array

# time complexity: O(n)
# space complexity: O(1)

test1 = [-1,0,1,-1,0,1,-1,0,0,0,1,1,1]
test2 = []
test3 = [-1,0]

print(Solution().rainbowSort(test1))
print(Solution().rainbowSort(test2))
print(Solution().rainbowSort(test3))