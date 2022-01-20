// Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Author : Hamza Mogni
// Date   : 2022-01-20

/*****************************************************************************************************
 *
 * Given a string s, find the length of the longest substring without repeating characters.
 *
 * Example 1:
 *
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 * Example 2:
 *
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 * Example 3:
 *
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 *
 * Constraints:
 *
 * 	0 <= s.length <= 5 * 10^4
 * 	s consists of English letters, digits, symbols and spaces.
 ******************************************************************************************************/

#include <iostream>
#include <unordered_map>
#include <assert.h>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> char_pos;

        int ptr1 = 0, ptr2 = 0;
        int length = 0;

        while (ptr2 < s.length())
        {
            if (char_pos.find(s[ptr2]) != char_pos.end())
            {
                if (char_pos[s[ptr2]] > ptr1)
                {
                    ptr1 = char_pos[s[ptr2]];
                }
            }

            if (ptr2 - ptr1 + 1 > length)
            {
                length = ptr2 - ptr1 + 1;
            }

            char_pos[s[ptr2]] = ptr2 + 1;
            ptr2++;
        }

        return length;
    }
};

int main()
{
    Solution s = Solution();

    int t1 = s.lengthOfLongestSubstring("abcabcbb");
    int t2 = s.lengthOfLongestSubstring("bbbbb");
    int t3 = s.lengthOfLongestSubstring("pwwkew");

    assert(t1 == 3);
    assert(t2 == 1);
    assert(t3 == 3);

    return 0;
}
