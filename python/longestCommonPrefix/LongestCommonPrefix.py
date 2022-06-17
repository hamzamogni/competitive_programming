#!/usr/bin/python
# Source : https://leetcode.com/problems/longest-common-prefix/
# Author : Hamza Mogni
# Date   : 2022-06-17

##################################################################################################### 
#
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# Constraints:
# 
# 	1 <= strs.length <= 200
# 	0 <= strs[i].length <= 200
# 	strs[i] consists of only lowercase English letters.
#####################################################################################################

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            We iterate over all given strings
            and we compare each character position,
            if we find a character that doesn't repeat
            at the same position through all strings we
            return empty strings, otherwise we return the
            current prefix.

            Complexity:
                - Time: o(S) # S is the number of strings in input
                - Space: o(1)
        """
        common_prefix = ""

        for idx in range(len(strs[0])):
            for word in strs:
                if idx == len(word) or word[idx] != strs[0][idx]:
                    return common_prefix
            common_prefix += strs[0][idx]

        return common_prefix

s = Solution()

t1 = s.longestCommonPrefix(["flower", "flow", "flight"])
assert(t1 == "fl")

t2 = s.longestCommonPrefix(["dog","racecar","car"])
assert(t2 == "")
