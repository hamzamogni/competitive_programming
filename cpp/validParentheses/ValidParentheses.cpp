// Source : https://leetcode.com/problems/valid-parentheses/
// Author : Hamza Mogni
// Date   : 2022-03-13

/***************************************************************************************************** 
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
 * input string is valid.
 * 
 * An input string is valid if:
 * 
 * 	Open brackets must be closed by the same type of brackets.
 * 	Open brackets must be closed in the correct order.
 * 
 * Example 1:
 * 
 * Input: s = "()"
 * Output: true
 * 
 * Example 2:
 * 
 * Input: s = "()[]{}"
 * Output: true
 * 
 * Example 3:
 * 
 * Input: s = "(]"
 * Output: false
 * 
 * Constraints:
 * 
 * 	1 <= s.length <= 10^4
 * 	s consists of parentheses only '()[]{}'.
 ******************************************************************************************************/


#include <iostream>
#include <assert.h>
#include <unordered_map>
#include <stack>

using namespace std;

class Solution
{
public:
    /**
     * We will use a stack and hashmap to solve this problem
     * we will iterate over our string as long as closing
     * parentheses keep matching with the last opened parenthese
     * (which we retreive from the stack).
     * 
     * we immediately return false when we find an inconsistency.
     * 
     * Complexity:
     *      Time: o(n)
     *      Space: o(n)
     **/
    bool isValid(string s) {
        unordered_map<char, char> parentheses = {
            {']', '['},
            {'}', '{'},
            {')', '('},
        };

        stack<char> visited;

        for (char chr: s) {
            if (parentheses.find(chr) == parentheses.end()) {
                visited.push(chr);
            } else {
                if (visited.empty()) {
                    return false;
                }

                if (parentheses[chr] == visited.top()) {
                    visited.pop();
                    continue;
                }
                
                return false;
            }
        }

        if (visited.empty()) {
            return true;
        }
        
        return false;
    }
};

int main()
{
    Solution s = Solution();
    bool t1 = s.isValid("()");
    bool t2 = s.isValid("(){}[]");
    bool t3 = s.isValid("(]");
    bool t4 = s.isValid("]");
    
    assert(t1 == true);
    assert(t2 == true);
    assert(t3 == false);
    assert(t4 == false);
    return 0;
}