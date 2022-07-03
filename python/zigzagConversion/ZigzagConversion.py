#!/usr/bin/python
# Source : https://leetcode.com/problems/zigzag-conversion/
# Author : Hamza Mogni
# Date   : 2022-07-03

##################################################################################################### 
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# Example 2:
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
# Example 3:
# 
# Input: s = "A", numRows = 1
# Output: "A"
# 
# Constraints:
# 
# 	1 <= s.length <= 1000
# 	s consists of English letters (lower-case and upper-case), ',' and '.'.
# 	1 <= numRows <= 1000
#####################################################################################################


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
            We iterate over the string and keep track
            of which row a character belongs to. We
            know that by checking wheter we are in
            a column or diagonal.

            The final step is to join the constructed
            row in one single string.

            Complexity:
                - Time: o(n)
                - Space: o(n) 

        """
        if numRows == 1:
            return s

        slices = [""] * min(len(s), numRows)


        current_row = 0
        is_diagonal = True

        for character in s:
            slices[current_row] += character

            if current_row in (0, numRows - 1):
                is_diagonal = not is_diagonal

            if is_diagonal:
                current_row -= 1
            else:
                current_row += 1

        return ''.join(slices)

s = Solution()

T1 = s.convert("PAYPALISHIRING", 4)
assert T1 == "PINALSIGYAHRPI"

T1 = s.convert("PAYPALISHIRING", 1)
assert T1 == "PAYPALISHIRING"
