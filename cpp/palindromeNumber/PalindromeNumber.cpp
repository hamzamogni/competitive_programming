// Source : https://leetcode.com/problems/palindrome-number/
// Author : Hamza Mogni
// Date   : 2022-03-13

/***************************************************************************************************** 
 *
 * Given an integer x, return true if x is palindrome integer.
 * 
 * An integer is a palindrome when it reads the same backward as forward.
 * 
 * 	For example, 121 is a palindrome while 123 is not.
 * 
 * Example 1:
 * 
 * Input: x = 121
 * Output: true
 * Explanation: 121 reads as 121 from left to right and from right to left.
 * 
 * Example 2:
 * 
 * Input: x = -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it 
 * is not a palindrome.
 * 
 * Example 3:
 * 
 * Input: x = 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 * 
 * Constraints:
 * 
 * 	-2^31 <= x <= 2^31 - 1
 * 
 * Follow up: Could you solve it without converting the integer to a string?
 ******************************************************************************************************/


#include <iostream>
#include <assert.h>

#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    /**
     * We will reverse the input number and then 
     * we check if the reversed int is equal to the original one.
     * 
     * while doing that we will check for overflow before making the computation.
     * 
     * Complexity:
     *      Time: o(log10(n))  (we divide by 10 in each iteration)
     *      Space: o(1)
     **/
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int reversed = 0,
            current = 0,
            input = x;

        while (input != 0) {
            current = input % 10;
            input /= 10;

            // Check for overflow before actually multiplying by 10
            if (
                (reversed > INT_MAX / 10 || reversed == INT_MAX / 10 && current > 7) ||
                (reversed < INT_MIN / 10 || reversed == INT_MIN / 10 && current < -8) 
            ) {
                return false;
            }

            reversed = reversed * 10 + current;
        }

        if (reversed == x) {
            return true;
        }

        return false;


    }
};

int main()
{
    Solution s = Solution();
    bool t1 = s.isPalindrome(-25);
    assert(t1 == false);

    bool t2 = s.isPalindrome(125);
    assert(t2 == false);


    bool t3 = s.isPalindrome(121);
    assert(t3 == true);


    bool t4 = s.isPalindrome(5);
    assert(t4 == true);

    bool t5 = s.isPalindrome(1234567899);
    assert(t5 == false);

    bool t6 = s.isPalindrome(88888);
    assert(t6 == true);

    return 0;
}