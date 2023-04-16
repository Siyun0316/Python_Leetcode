# find coommon number of two arrays
#Both arrays are not null.
#There are no duplicate numbers in each of the two arrays respectively.
class Solution(object):
    def common(self, a1, a2):
        set_a1 = set(a1)
        res = []
        for x in a2:
            if x in set_a1:
                res.append(x)
        return sorted(res)
    #   return sorted(x for x in a2 if x in set_a1)

# time complexity O(m+n)
# space complexity O(m)

test_a = [1,2,3,4,5,6,7,8,9]
test_b = [3,5,7,9,11,13,15]
test_c = []
print (Solution().common(test_a,test_b))
print (Solution().common(test_a,test_c))
