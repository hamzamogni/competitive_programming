# Source : https://leetcode.com/problems/pascals-triangle
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
#
# 	1 <= numRows <= 30
#####################################################################################################

from typing import List


class Solution:
    # Time: o(n²)
    # Space: o(n²)
    def generate(self, numRows: int) -> List[List[int]]:
        '''
            we will make numRows iterations, the first line
            in a Pascal triangle is always [[1]] so will start
            with that. 

            Then, at each iteration we will save the last calculated
            row and base on it we will calculate the next row. We will make
            sure to start and end every line with the number 1.
        '''
        result = [[1]]

        if numRows == 1:
            return result

        for i in range(1, numRows):
            previous = result[i-1]

            current = [1]

            for j in range(1, len(previous)):
                current.append(previous[j-1] + previous[j])

            current.append(1)

            result.append(current)

        return result


s = Solution()
test1 = s.generate(5)
test2 = s.generate(1)

assert test1 == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert test2 == [[1]]
