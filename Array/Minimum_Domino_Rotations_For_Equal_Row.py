'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
as indicated by the second figure.

Example 2:
'''

class Solution(object):
    def minDominoRotations(self,  A,  B):
        if len(A) != len(B):
            return 0
        def helper(k):
            rot_a = 0
            rot_b = 0
            for i in range(len(A)):
                if A[i] != k and B[i] != k:
                    return -1
                elif B[i] !=k:
                    rot_b +=1
                elif A[i] !=k:
                    rot_a +=1
            return min(rot_a, rot_b)
        _min = helper(A[0])
        if _min != -1 or A[0] == B[0]:
            return _min
        else:
            return helper(B[0])


# time complexity O(n)
# space complexity O(1)
print(Solution().minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))

print(Solution().minDominoRotations([3,5,1,2,3],[3,6,3,3,4]))

print(Solution().minDominoRotations([2,2,2,1,1,2,2],[2,2,2,2,2,1,2]))




