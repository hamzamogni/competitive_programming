"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

"""
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
