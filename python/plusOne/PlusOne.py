# Source : https://leetcode.com/problems/plus-one/
# Author : Hamza Mogni
# Date   : 2022-06-02

##################################################################################################### 
#
# You are given a large integer represented as an integer array digits, where each digits[i] is the 
# i^th digit of the integer. The digits are ordered from most significant to least significant in 
# left-to-right order. The large integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of digits.
# 
# Example 1:
# 
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# 
# Example 2:
# 
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# 
# Example 3:
# 
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
# 
# Constraints:
# 
# 	1 <= digits.length <= 100
# 	0 <= digits[i] <= 9
# 	digits does not contain any leading 0's.
#####################################################################################################

from math import remainder
from typing import List
from unicodedata import digit

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = digits[len(digits) - 1] + 1

        if plus_one < 10:
            digits[len(digits) - 1] = plus_one
            return digits


        digits[len(digits) - 1] = 0
        remainder = 1

        i = len(digits) - 2

        while i > -1:
            if remainder == 0:
                break

            num = digits[i] + remainder
            if num == 10:
                digits[i], remainder = 0, 1
            else:
                digits[i], remainder = num, 0

            i -= 1
        if remainder == 1:
            digits.insert(0, 1)
        return digits

s = Solution()
s.plusOne([9, 9, 9])