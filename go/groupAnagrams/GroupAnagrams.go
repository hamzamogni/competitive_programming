// Source : https://leetcode.com/problems/group-anagrams/
// Author : Hamza Mogni
// Date   : 2023-05-05

/*****************************************************************************************************
 *
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 * typically using all the original letters exactly once.
 *
 * Example 1:
 * Input: strs = ["eat","tea","tan","ate","nat","bat"]
 * Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 * Example 2:
 * Input: strs = [""]
 * Output: [[""]]
 * Example 3:
 * Input: strs = ["a"]
 * Output: [["a"]]
 *
 * Constraints:
 *
 * 	1 <= strs.length <= 10^4
 * 	0 <= strs[i].length <= 100
 * 	strs[i] consists of lowercase English letters.
 ******************************************************************************************************/

package main

import "fmt"

func main() {
	result := groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"})
	fmt.Println(result)

}

// we take advantage of the definition of anagrams,
// two anagrams will always have same count of letters
// thus for each word we create a array of 26 ints, counting
// frequencies of letters. We use a map to group words that
// have the same array of counts.
//
//	Complexity:
//		Time: o(nk) ==> n is number of words, k is length of longest word
//		Space: o(nk) ==> for creating the hashmap
func groupAnagrams(strs []string) [][]string {
	countHash := map[[26]int][]string{}

	for _, str := range strs {
		hash := [26]int{}
		for i := 0; i < len(str); i++ {
			hash[str[i]-'a']++
		}
		countHash[hash] = append(countHash[hash], str)
	}

	result := [][]string{}

	for _, group := range countHash {
		result = append(result, group)
	}

	return result
}
