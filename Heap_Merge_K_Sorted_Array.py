# Merge K Sorted Array
# Merge K sorted array into one big sorted array in ascending order.
# Assumptions
# The input arrayOfArrays is not null, none of the arrays is null either.

import heapq
class Solution(object):
    def merge(self, arrayOfArrays):
        """
        input: int[][] arrayOfArrays
        return: int[]
        """
        if not arrayOfArrays:
            return []
        tmp = []
        for i in range(len(arrayOfArrays)):
            if len(arrayOfArrays[i]) > 0:
                tmp.append((arrayOfArrays[i][0], i, 0))
        heapq.heapify(tmp)
        res = []
        while tmp:
            cur, row, col = heapq.heappop(tmp)
            res.append(cur)
            if len(arrayOfArrays[row]) > col+1:
                heapq.heappush(tmp,(arrayOfArrays[row][col+1], row, col+1))
        return res

# time complexity O(nlogk)
# space complexity O(k)

import unittest

class testMerge(unittest.TestCase):
    def test_merge(self):
        solution = Solution()
        # Test case 1
        arrayOfArrays = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(solution.merge(arrayOfArrays), expected_output)

        # Test case 2
        arrayOfArrays = [[], [], []]
        expected_output = []
        self.assertEqual(solution.merge(arrayOfArrays), expected_output)

        # Test case 3
        arrayOfArrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(solution.merge(arrayOfArrays), expected_output)

        # Test case 4
        arrayOfArrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(solution.merge(arrayOfArrays), expected_output)

        # Test case 5
        arrayOfArrays = [[], [1, 2, 3], [4, 5, 6]]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(solution.merge(arrayOfArrays), expected_output)

        # Test case 6
        arrayOfArrays = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected_output = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(solution.merge(arrayOfArrays), expected_output)


