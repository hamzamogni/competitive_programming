// Source : https://leetcode.com/problems/top-k-frequent-elements
// Author : Hamza Mogni
// Date   : 2023-05-07

/*****************************************************************************************************
 *
 * Given an integer array nums and an integer k, return the k most frequent elements. You may return
 * the answer in any order.
 *
 * Example 1:
 * Input: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 * Example 2:
 * Input: nums = [1], k = 1
 * Output: [1]
 *
 * Constraints:
 *
 * 	1 <= nums.length <= 10^5
 * 	-10^4 <= nums[i] <= 10^4
 * 	k is in the range [1, the number of unique elements in the array].
 * 	It is guaranteed that the answer is unique.
 *
 * Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's
 * size.
 ******************************************************************************************************/

package main

import "fmt"

func main() {
	fmt.Println(topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2))
}

// we iterate over array to count frequency of each number,
// then we group numbers with same frequency in a slice
// each group's index is the frequency.
// we then iterate on the slice constructing the final result.
//
//	Complexity:
//		Time: o(n log(k))
//		Space: o(n)
func topKFrequent(nums []int, k int) []int {
	numberCount := map[int]int{}

	for _, n := range nums {
		numberCount[n]++
	}

	slice := make([][]int, len(nums)+1)
	for num, count := range numberCount {
		slice[count] = append(slice[count], num)
	}

	result := []int{}
	for i := len(slice) - 1; i >= 0; i-- {
		result = append(result, slice[i]...)
		if len(result) == k {
			return result
		}

	}

	return result

}
