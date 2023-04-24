# Fibonacci Number
# Get the Kth number in the Fibonacci Sequence.
# (K is 0-indexed, the 0th Fibonacci number is 0 and the 1st Fibonacci number is 1).
# Examples
# 0th fibonacci number is 0
# 1st fibonacci number is 1
# 2nd fibonacci number is 1
# 3rd fibonacci number is 2
# 6th fibonacci number is 8
#  Corner Cases
# What if K < 0? in this case, we should always return 0.
# Is it possible the result fibonacci number is overflowed?
# We can assume it will not be overflowed when we solve this problem on this online judge,
# but we should also know that it is possible to get an overflowed number,
# and sometimes we will need to use something like BigInteger.
import unittest


class Solution(object):
    def fibonacci(self, K):
        """
        input: int K
        return: long
        """
        # write your solution here
        if K <= 0:
            return 0
        if K == 1 or K == 2:
            return 1
        lres = self.fibonacci(K - 2)
        rres = self.fibonacci(K - 1)
        return lres + rres

# time complexity O(2^k)
# space complexity O(k)

    def fibonacci2(self, K):
        """
        input: int K
        return: long
        """
        # write your solution here
        if K <= 0:
            return 0
        if K == 1 or K == 2:
            return 1
        res, tmp = 0, 1
        for i in range(K):
            res, tmp = res+tmp, res
        return res

# time complexity O(K)
# space complexity O(1)

class Test(unittest.TestCase):
    def test_fibonacci(self):

        _inp = 6
        _out = 8
        self.assertEqual(Solution().fibonacci(_inp), _out)
        self.assertEqual(Solution().fibonacci2(_inp), _out)

        _inp = 0
        _out = 0
        self.assertEqual(Solution().fibonacci(_inp), _out)
        self.assertEqual(Solution().fibonacci2(_inp), _out)

        _inp = 2
        _out = 1
        self.assertEqual(Solution().fibonacci(_inp), _out)
        self.assertEqual(Solution().fibonacci2(_inp), _out)

        _inp = 10
        _out = 55
        self.assertEqual(Solution().fibonacci(_inp), _out)
        self.assertEqual(Solution().fibonacci2(_inp), _out)





