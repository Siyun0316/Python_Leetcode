'''
1052. Grumpy Bookstore Owner
https://leetcode.com/problems/grumpy-bookstore-owner/
'''


class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:

        if len(customers) != len(grumpy):
            return -1

        # grumpy as mask, divide the possible unhappy costumers and happy costumers
        unhappy = [customers[i] * grumpy[i] for i in range(len(grumpy))]
        happy = sum(customers) - sum(unhappy)

        _max = sum(unhappy[:minutes])
        tmp = sum(unhappy[:minutes])

        for i in range(minutes, len(grumpy)):
            tmp = tmp + unhappy[i] - unhappy[i - minutes]
            _max = max(_max, tmp)

        return _max + happy

# time complexity O(n)
# space complexity O(n)
    def maxSatisfied2(self, customers, grumpy, minutes: int) -> int:
        if len(customers) != len(grumpy):
            return -1
        happy = 0
        unhappy = 0
        max_unhappy = 0
        for i in range(len(grumpy)):
            if i >= minutes:
                unhappy += grumpy[i]*customers[i] - grumpy[i-minutes]*customers[i-minutes]
            else:
                unhappy += grumpy[i]*customers[i]
            happy += ((1-grumpy[i])*customers[i])
            max_unhappy = max(max_unhappy, unhappy)
        return happy + max_unhappy

# time complexity O(n)
# space complexity O(1)

print(Solution().maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1], 3))
print(Solution().maxSatisfied2([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1], 3))
print(Solution().maxSatisfied([1,0,1],[0,1,0], 3))
print(Solution().maxSatisfied2([1,0,1],[0,1,0], 3))
