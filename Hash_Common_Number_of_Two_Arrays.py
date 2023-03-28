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
