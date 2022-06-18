#!/usr/bin/python
# Source : https://leetcode.com/problems/binary-search
# Author : Hamza Mogni
# Date   : 2022-06-18

##################################################################################################### 
#
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a 
# function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Example 1:
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# Example 2:
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^4
# 	-10^4 < nums[i], target < 10^4
# 	All the integers in nums are unique.
# 	nums is sorted in ascending order.
#####################################################################################################

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            This is a simple and straightforward implementation
            of binary search.

            Complexity:
                - Time: o(log(n))
                - Space: o(1)
        """
        start, end = 0, len(nums)-1

        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1

        return -1

s = Solution()
t1 = s.search([1, 2, 3, 4, 5], 9)
assert(t1 == -1)

t2 = s.search([1, 2, 3, 4, 5], 5)
assert(t2 == 4)
