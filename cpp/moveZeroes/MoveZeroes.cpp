// Source : https://leetcode.com/problems/move-zeroes/description/
// Author : Hamza Mogni
// Date   : 2023-02-24

/***************************************************************************************************** 
 *
 * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of 
 * the non-zero elements.
 * 
 * Note that you must do this in-place without making a copy of the array.
 * 
 * Example 1:
 * Input: nums = [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 * Example 2:
 * Input: nums = [0]
 * Output: [0]
 * 
 * Constraints:
 * 
 * 	1 <= nums.length <= 10^4
 * 	-2^31 <= nums[i] <= 2^31 - 1
 * 
 * Follow up: Could you minimize the total number of operations done?
 ******************************************************************************************************/

#include <vector>
#include <iostream>

using namespace std;

class Solution {
    /**
     * We use a two pointers approach.
     * We bring all non-zero values to beginning of array then fill
     * remaining part of array with zeroes.
     *
     * Complexity:
     *      Time: o(n).
     *      Space: o(1).
     */
public:
    void moveZeroes(vector<int>& nums) {
        // bring all non-zero values to beginning of array
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != 0) {
                nums[i++] = nums[j];
            }
        }

        // fill remaining positions with 0
        for (int k = i; k < nums.size(); k++){
            nums[k] = 0;
        }
    }
};

int main() {
    Solution s = Solution();

    vector<int> input = {1, 0, 12, 0, 0, 14};
    s.moveZeroes(input);

    return 0;
}