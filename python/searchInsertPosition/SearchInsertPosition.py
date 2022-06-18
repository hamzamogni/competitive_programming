# Source : https://leetcode.com/problems/search-insert-position
# Author : Hamza Mogni
# Date   : 2022-06-18

##################################################################################################### 
#
# Given a sorted array of distinct integers and a target value, return the index if the target is 
# found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Example 1:
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# Example 2:
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# Example 3:
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^4
# 	-10^4 <= nums[i] <= 10^4
# 	nums contains distinct values sorted in ascending order.
# 	-10^4 <= target <= 10^4
#####################################################################################################


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            We solve this using binary search.
            If the iterations end and we haven't
            found our target, then it should be
            inserted at the lower-bound of the
            last iteration range.

            Complexity:
                - Time: o(log(n))
                - Space: o(1)
        """
        start, end = 0, len(nums)-1

        while start <= end:
            middle = start + (end - start) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1

        return start
