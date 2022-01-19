# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
#
# 	0 <= s.length <= 5 * 10^4
# 	s consists of English letters, digits, symbols and spaces.
#####################################################################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}

        ptr1 = 0
        ptr2 = 0

        length = 0

        while ptr2 < len(s):
            if s[ptr2] in char_pos:
                if char_pos[s[ptr2]] > ptr1:
                    ptr1 = char_pos[s[ptr2]]

            if ptr2 - ptr1 + 1 > length:
                length = ptr2 - ptr1 + 1

            char_pos[s[ptr2]] = ptr2+1

            ptr2 += 1
        return length


s = Solution()

print(s.lengthOfLongestSubstring(
    "tmmzuxt"))
