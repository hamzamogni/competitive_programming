# Source : https://leetcode.com/problems/two-sum
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same
# element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
#
# 	2 <= nums.length <= 10^4
# 	-10^9 <= nums[i] <= 10^9
# 	-10^9 <= target <= 10^9
# 	Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
#####################################################################################################

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            We iterate over nums, the visited hash map will contain
            numbers we have already visited.

            while iterating, we look if the difference between current number
            and target already exists in our hash map, if yes then we return the solution,
            if not we add the current number and its index to the hashmap
        """

        visited = {}

        for idx, num in enumerate(nums):
            searching = target - num

            if searching in visited:
                return [idx, visited[searching]]

            visited[num] = idx


s = Solution()
print(s.twoSum([1, 1], 2))
