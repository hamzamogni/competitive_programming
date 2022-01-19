# Source : https://leetcode.com/problems/valid-anagram
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
#
# 	1 <= s.length, t.length <= 5 * 10^4
# 	s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such
# a case?
#####################################################################################################

class Solution:
    # Time: o(n)
    # Space: o(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = dict()

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1

        for count in char_count.values():
            if count != 0:
                return False

        return True


s = Solution()
test1 = s.isAnagram("anagram", "nagaram")
test2 = s.isAnagram("rat", "car")

assert test1 == True
assert test2 == False
