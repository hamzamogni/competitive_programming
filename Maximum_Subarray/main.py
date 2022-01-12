"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]

        current = 0

        for nbr in nums:
            if current < 0:
                current = 0

            current += nbr

            maximum = max(maximum, current)

        return maximum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
