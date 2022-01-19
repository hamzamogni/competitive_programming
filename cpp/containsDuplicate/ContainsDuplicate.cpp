// Source : https://leetcode.com/problems/contains-duplicate
// Author : Hamza Mogni
// Date   : 2022-01-19

/***************************************************************************************************** 
 *
 * Given an integer array nums, return true if any value appears at least twice in the array, and 
 * return false if every element is distinct.
 * 
 * Example 1:
 * Input: nums = [1,2,3,1]
 * Output: true
 * Example 2:
 * Input: nums = [1,2,3,4]
 * Output: false
 * Example 3:
 * Input: nums = [1,1,1,3,3,4,3,2,4,2]
 * Output: true
 * 
 * Constraints:
 * 
 * 	1 <= nums.length <= 10^5
 * 	-10^9 <= nums[i] <= 10^9
 ******************************************************************************************************/

#include <iostream>
#include <vector>
#include <set>
#include <assert.h>

using namespace std;

class Solution
{
public:
    // Time: o(n)
    // Space: o(n)
    bool containsDuplicate(vector<int> &nums)
    {
        set<int> visited;

        for (int nbr : nums)
        {
            if (visited.find(nbr) != visited.end())
            {
                return true;
            }

            visited.insert(nbr);
        }

        return false;
    }
};

int main()
{
    Solution s = Solution();

    vector<int> input = {1, 2, 3, 1};
    bool output = s.containsDuplicate(input);
    assert(output == true);
    return 0;
}