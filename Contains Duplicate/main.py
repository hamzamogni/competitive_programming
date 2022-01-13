"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.


"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        for nbr in nums:
            if nbr in visited:
                return True

            visited.add(nbr)

        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
