#!/usr/bin/python
# Source : https://leetcode.com/problems/first-bad-version
# Author : Hamza Mogni
# Date   : 2022-06-18

##################################################################################################### 
#
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the 
# latest version of your product fails the quality check. Since each version is developed based on 
# the previous version, all the versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
# all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a 
# function to find the first bad version. You should minimize the number of calls to the API.
# 
# Example 1:
# 
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# 
# Example 2:
# 
# Input: n = 1, bad = 1
# Output: 1
# 
# Constraints:
# 
# 	1 <= bad <= n <= 2^31 - 1
#####################################################################################################


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
            This problem can be solved using 
            a binary search approach, since we know
            that if a version is good, then all preceding
            versions are also good.
            This problem is similar to how the command `git bisect`
            works to find the first bad commit in history.

            Comlexity:
                - Time: o(log(n))
                - Space: o(1)
        """
        start, end = 1, n

        while (start < end):
            middle = start + (end - start) // 2

            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1

        return start
