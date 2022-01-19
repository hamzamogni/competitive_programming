# Source : https://leetcode.com/problems/intersection-of-two-arrays-ii
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in
# the result must appear as many times as it shows in both arrays and you may return the result in
# any order.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
# Constraints:
#
# 	1 <= nums1.length, nums2.length <= 1000
# 	0 <= nums1[i], nums2[i] <= 1000
#
# Follow up:
#
# 	What if the given array is already sorted? How would you optimize your algorithm?
# 	What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 	What if elements of nums2 are stored on disk, and the memory is limited such that you
# cannot load all elements into the memory at once?
#####################################################################################################

from typing import List


class Solution:
    # Time: o(m + n)
    # Space: o(min(m, n))
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
            We iterate over the first array, and count how many times
            each number appeard (we store that in a map),
            then we iterate over the second array, when we find a number
            that exists in our map and the count is bigger than 0 then we
            add that number to our result.

            To keep our map the smallest possible, and decrease space complexity,
            we will recall our function and ensure we always give the smallest
            array first
        '''

        if (len(nums1) > len(nums2)):
            return self.intersect(nums2, nums1)

        result = list()
        visited = dict()

        for a in nums1:
            if a not in visited:
                visited[a] = 1
            else:
                visited[a] += 1

        for a in nums2:
            count = visited.get(a, 0)

            if count > 0:
                result.append(a)
                visited[a] -= 1

        return result


s = Solution()
t1 = s.intersect([9, 4, 9, 8, 4], [4, 9, 5])
t2 = s.intersect([1, 2, 2, 1], [2, 2])

assert sorted(t1) == sorted([4, 9])
assert sorted(t2) == sorted([2, 2])
