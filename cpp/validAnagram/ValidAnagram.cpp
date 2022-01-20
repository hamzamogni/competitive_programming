// Source : https://leetcode.com/problems/valid-anagram
// Author : Hamza Mogni
// Date   : 2022-01-20

/***************************************************************************************************** 
 *
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
 * 
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
 * typically using all the original letters exactly once.
 * 
 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * Constraints:
 * 
 * 	1 <= s.length, t.length <= 5 * 10^4
 * 	s and t consist of lowercase English letters.
 * 
 * Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such 
 * a case?
 ******************************************************************************************************/
#include <iostream>
#include <string>
#include <unordered_map>
#include <assert.h>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }

        unordered_map<char, int> char_count;

        for (auto &ch : s)
        {
            if (char_count.find(ch) != char_count.end())
            {
                char_count[ch]++;
            }
            else
            {
                char_count[ch] = 1;
            }
        }

        for (auto &ch : t)
        {
            if (char_count.find(ch) == char_count.end())
            {
                return false;
            }
            else
            {
                char_count[ch]--;
            }
        }

        for (auto const &x : char_count)
        {
            if (x.second != 0)
            {
                return false;
            }
        }

        return true;
    }
};

int main()
{
    Solution s = Solution();

    bool t1 = s.isAnagram("anagram", "nagaram");
    bool t2 = s.isAnagram("rat", "car");

    assert(t1 == true);
    assert(t2 == false);
}