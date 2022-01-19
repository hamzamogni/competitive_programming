# Source : https://leetcode.com/problems/reshape-the-matrix
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new
# one with a different size r x c keeping its original data.
#
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the
# number of columns of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original matrix in the same
# row-traversing order as they were.
#
# If the reshape operation with given parameters is possible and legal, output the new reshaped
# matrix; Otherwise, output the original matrix.
#
# Example 1:
#
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
#
# Example 2:
#
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
#
# Constraints:
#
# 	m == mat.length
# 	n == mat[i].length
# 	1 <= m, n <= 100
# 	-1000 <= mat[i][j] <= 1000
# 	1 <= r, c <= 300
#####################################################################################################

from typing import List


class Solution:
    # Time: o(mn)
    # Space: o(mn)
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if r * c != m * n:
            return mat

        # We create our (r, c) shaped result
        result = [[0] * c] * r

        cur_row = 0
        cur_col = 0

        for i in range(m):
            for j in range(n):
                result[cur_row][cur_col] = mat[i][j]
                cur_col += 1

                if cur_col == c:
                    cur_col = 0
                    cur_row += 1

        return result


s = Solution()
test1 = s.matrixReshape([[1, 2], [3, 4]], 1, 4)
test2 = s.matrixReshape([[1, 2], [3, 4]], 2, 4)

assert test1 == [[1, 2, 3, 4]]
assert test2 == [[1, 2], [3, 4]]
