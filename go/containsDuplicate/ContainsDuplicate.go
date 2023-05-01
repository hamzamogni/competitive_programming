// Source : https://leetcode.com/problems/contains-duplicate/
// Author : Hamza Mogni
// Date   : 2023-05-01

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

package main

import "fmt"

func containsDuplicate(nums []int) bool {
	exist := make(map[int]bool)

	for _, num := range nums {
		if exist[num] {
			return true
		}

		exist[num] = true
	}

	return false

}

func main() {
	testCases := [][]int{
		{1, 2, 3, 1},
		{1, 2, 3, 4},
		{1, 1, 1, 3, 3, 4, 3, 2, 4, 2},
	}

	for _, testCase := range testCases {
		fmt.Println(containsDuplicate(testCase))
	}

}
