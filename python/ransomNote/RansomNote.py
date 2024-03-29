# Source : https://leetcode.com/problems/ransom-note
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from
# magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
# Constraints:
#
# 	1 <= ransomNote.length, magazine.length <= 10^5
# 	ransomNote and magazine consist of lowercase English letters.
#####################################################################################################

class Solution:
    # Time: o(n)
    # Space: o(n)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = dict()

        # we count how many times each letter appears in magazine
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1

        # we count how many times each letter appears in ransomNote
        # if the letter doesnt exist in magazine we return False
        # if we use more of a letter than exists in magazine we return False
        for char in ransomNote:
            if char not in char_count:
                return False

            char_count[char] -= 1

            if char_count[char] < 0:
                return False

        return True


s = Solution()
test1 = s.canConstruct("a", "b")
test2 = s.canConstruct("aa", "ab")
test3 = s.canConstruct("aa", "aab")

assert test1 == False
assert test2 == False
assert test3 == True
