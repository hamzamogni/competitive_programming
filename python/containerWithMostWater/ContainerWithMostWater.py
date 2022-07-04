#!/usr/bin/python
# Source : https://leetcode.com/problems/container-with-most-water
# Author : Hamza Mogni
# Date   : 2022-07-04

##################################################################################################### 
#
# You are given an integer array height of length n. There are n vertical lines drawn such that the 
# two endpoints of the i^th line are (i, 0) and (i, height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the container contains the 
# most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# Example 1:
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
# the max area of water (blue section) the container can contain is 49.
# 
# Example 2:
# 
# Input: height = [1,1]
# Output: 1
# 
# Constraints:
# 
# 	n == height.length
# 	2 <= n <= 10^5
# 	0 <= height[i] <= 10^4
#####################################################################################################

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
            We follow a two pointers approach,
            we start at the borders of the array
            and move our pointers whenever we find
            a line that's higher than the current
            shortest line.

            Complexity:
                - Time: o(n)
                - Space: o(1)
        '''
        start, end = 0, len(height)-1

        area = (end - start) * min(height[start], height[end])

        while start < end:
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

            cur_arr = (end - start) * min(height[start], height[end])
            area = max(cur_arr, area)

        return area

s = Solution()
T1 = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
assert T1 == 49

T2 = s.maxArea([1, 1])
assert T2 == 1
