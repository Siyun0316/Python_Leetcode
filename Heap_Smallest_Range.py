# Smallest Range
# Given k sorted integer arrays, pick k elements (one element from each of sorted arrays), what is the smallest range.
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
# Assumptions:
# k >= 2
# None of the k arrays is null or empty

import heapq
class Solution(object):
    def smallestRange(self, arrays):
        """
        input: int[][] arrays
        return: int[]
        """
        if not arrays:
            return []
        res = [float('-inf'), float('inf')]
        _max = float('-inf')
        k = len(arrays)
        tmp = []
        for i in range(k):
            if len(arrays[i])>0:
                tmp.append((arrays[i][0], i, 0))
                _max = max(_max,arrays[i][0])
        heapq.heapify(tmp)
        while len(tmp) ==k:
            _min, r, c = heapq.heappop(tmp)
            if _max-_min < res[1]-res[0]:
                res = [_min, _max]

            if len(arrays[r])>c+1:
                heapq.heappush(tmp,(arrays[r][c+1],r,c+1))
                _max = max(_max, arrays[r][c+1])

        return res

# time complexity O(k, nlogk)
# space complexity O(k)

import unittest

class testSmallestRange(unittest.TestCase):
    def test_smallestrange(self):
        solution = Solution()

        # test case
        arrayOfArrays = [[1,2,3],[4,5,6],[3,6,8]]
        expected_output = [3,4]
        self.assertEqual(solution.smallestRange(arrayOfArrays),expected_output)

        # Test case 1
        arrays = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        expected_output = [20, 24]
        self.assertEqual(solution.smallestRange(arrays), expected_output)

        # Test case 2
        arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [3, 7]
        self.assertEqual(solution.smallestRange(arrays), expected_output)

        # Test case 3
        arrays = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected_output = [4, 9]
        self.assertEqual(solution.smallestRange(arrays), expected_output)

        # Test case 4
        arrays = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected_output = [1, 1]
        self.assertEqual(solution.smallestRange(arrays), expected_output)
