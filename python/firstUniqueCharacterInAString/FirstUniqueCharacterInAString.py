# Source : https://leetcode.com/problems/first-unique-character-in-a-string
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given a string s, find the first non-repeating character in it and return its index. If it does not
# exist, return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
# Constraints:
#
# 	1 <= s.length <= 10^5
# 	s consists of only lowercase English letters.
#####################################################################################################

class Solution:
    # Time: o(n)
    # Space: o(n)
    def firstUniqChar(self, s: str) -> int:
        """
            We iterate over the string and count occurences
            of each character.

            then we reiterate over the string and return the
            first chracter that appeared only once in the string
        """
        char_count = dict()

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for idx, char in enumerate(s):
            if char_count[char] == 1:
                return idx

        return -1


s = Solution()
test1 = s.firstUniqChar("leetcode")
test2 = s.firstUniqChar("loveleetcode")
test3 = s.firstUniqChar("aabb")

assert test1 == 0
assert test2 == 2
assert test3 == -1
