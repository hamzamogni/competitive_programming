"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

"""


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
