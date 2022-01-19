# Source : https://leetcode.com/problems/search-a-2d-matrix
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the
# following properties:
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
# Example 1:
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
# Constraints:
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 100
# 	-10^4 <= matrix[i][j], target <= 10^4
#####################################################################################################

from typing import List


class Solution:
    # Time: o(log(n) + log(m))
    # Space: o(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            We will binary search the rows first for the one that may 
            contain our target, taking advanatage of the fact that 
            rows are also sorted with no overlap.

            if we find a possible row, we will run another binary search
            to look for our target in that row
        """
        rows, cols = len(matrix), len(matrix[0])

        upper, lower = 0, rows - 1
        while upper <= lower:
            row = (upper + lower) // 2

            if target > matrix[row][-1]:
                upper = row + 1
            elif target < matrix[row][0]:
                lower = row - 1
            else:
                break

        if upper > lower:
            return False

        beg, end = 0, cols - 1
        while beg <= end:
            current = (beg + end) // 2
            if target > matrix[row][current]:
                beg = current + 1
            elif target < matrix[row][current]:
                end = current - 1
            else:
                return True

        return False


s = Solution()
test1 = s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
test2 = s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)

assert test1 == True
assert test2 == False
