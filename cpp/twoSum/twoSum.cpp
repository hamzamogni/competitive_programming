/*
1. Two Sum
---------------

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

*/

#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> visited;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++)
        {
            int searching = target - nums[i];

            if (visited.find(searching) != visited.end())
            {
                return {i, visited[searching]};
            }

            visited[nums[i]] = i;
        }

        return {};
    }
};

int main()
{
    Solution s = Solution();
    vector<int> input = {1, 1};
    vector<int> output = s.twoSum(input, 2);

    for (int n : output)
    {
        cout << n << " ";
    }
}