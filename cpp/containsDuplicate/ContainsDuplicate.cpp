/***
 * 217. Contains Duplicate
 * 
 * Given an integer array nums, return true if any value appears at least twice
 * in the array, and return false if every element is distinct.
 ***/

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