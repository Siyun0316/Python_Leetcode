# Kth Largest Element in an Array
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        input: int[] nums, int k
        return: int
        """
        if len(nums)<k:
            return
        tmp = nums[:k]
        heapq.heapify(tmp)
        for x in nums[k:]:
            if x > tmp[0]:
                heapq.heappop(tmp)
                heapq.heappush(tmp,x)
        return tmp[0]

# time complexity O(nlogk) O(n)
# space complexity O(k) O(1)

import unittest

class TestFindKthLargest(unittest.TestCase):

    def test_findKthLargest(self):
        solution = Solution()

        # Test case 1
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected_output = 5
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

        # Test case 2
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected_output = 4
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

        # Test case 3
        nums = [1, 2, 3, 4, 5, 6]
        k = 1
        expected_output = 6
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

        # Test case 4
        nums = [1, 2, 3, 4, 5, 6]
        k = 6
        expected_output = 1
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

        # Test case 5
        nums = [1, 2, 3, 4, 5, 6]
        k = 7
        expected_output = None
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

        # Test case 6
        nums = []
        k = 1
        expected_output = None
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

        # Test case 7
        nums = [1]
        k = 1
        expected_output = 1
        self.assertEqual(solution.findKthLargest(nums, k), expected_output)

