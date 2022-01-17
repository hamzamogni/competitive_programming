'''
1. Two Sum
---------------

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

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
