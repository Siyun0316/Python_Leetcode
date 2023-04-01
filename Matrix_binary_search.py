
# Search in sorted 2D matrix
class Solution(object):
    def searchMatrix(self,matrix,target):
        '''
        :param matrix : list[list[int]]
        :param target : int
        :return : list[int]
        '''
        if not matrix:
            return [-1,-1]
        row = len(matrix)
        col = len(matrix[0])
        left,right = 0, row*col-1
        while left <= right:
            mid = (left+right)//2
            current_row = mid//col
            current_col = mid%col
            if matrix[current_row][current_col] == target:
                return [current_row,current_col]
            elif matrix[current_row][current_col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1,-1]
# time complexity O(log(row*col))
# space complexity O(1)

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = [[1],[2],[3]]
print(Solution().searchMatrix(a,6))
print(Solution().searchMatrix(a,13))
print(Solution().searchMatrix(a,9))
print(Solution().searchMatrix(b,3))
print(Solution().searchMatrix(b,1))

