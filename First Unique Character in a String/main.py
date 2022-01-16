"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character 
in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
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
