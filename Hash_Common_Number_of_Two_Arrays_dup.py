# find coommon number of two arrays
#Both arrays are not null.
#In any of the two arrays, there could be duplicate numbers.
class Solution(object):
    def common(self, a1, a2):
        h_a1 = {}
        for x in a1:
            if x in h_a1:
                h_a1[x]+=1
            else:
                h_a1[x] =1
        '''
        for x in a1:
            h_a1[x] = h_a1.get(x,0) + 1
        '''
        res = []
        for x in a2:
            if x in h_a1 and h_a1[x] >0:
                res.append(x)
                h_a1[x] -=1
        return sorted(res)


# time complexity O(m+n)
# space complexity O(m)

test_a = [1,2,3,4,5,6,7,7,7,8,9]
test_b = [3,5,7,7,9,11,13,15]
test_c = []
test_d = [7,7,7]
print (Solution().common(test_a,test_b))
print (Solution().common(test_a,test_c))
print (Solution().common(test_a,test_d))
