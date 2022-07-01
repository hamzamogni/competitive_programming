#!/usr/bin/python
# Source : https://leetcode.com/problems/roman-to-integer
# Author : Hamza Mogni
# Date   : 2022-07-01

##################################################################################################### 
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as 
# XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
# four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
# subtract it making four. The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:
# 
# 	I can be placed before V (5) and X (10) to make 4 and 9. 
# 	X can be placed before L (50) and C (100) to make 40 and 90. 
# 	C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# Given a roman numeral, convert it to an integer.
# 
# Example 1:
# 
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# 
# Example 2:
# 
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# 
# Example 3:
# 
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
# Constraints:
# 
# 	1 <= s.length <= 15
# 	s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# 	It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#####################################################################################################

class Solution:
    '''
        We loop over the roman letter from back to front,
        we keep adding to the result accordingly.
        We make sure to add the first digit too.

        Complexity:
            - Time: o(n)
            - Space: o(1)
    '''
    def romanToInt(self, s: str) -> int:
        digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        current_idx = len(s) - 1

        remainder = True

        while current_idx > 0:
            if digits[s[current_idx]] > digits[s[current_idx - 1]]:
                if current_idx == 1:
                    remainder = False

                total += digits[s[current_idx]] - digits[s[current_idx - 1]]
                current_idx -= 2
                continue

            total += digits[s[current_idx]]
            current_idx -= 1

        if remainder:
            total += digits[s[0]]

        return total

s = Solution()

t1 = s.romanToInt("III")
assert t1 == 3

t2 = s.romanToInt("MCMXCIV")
assert t2 == 1994
