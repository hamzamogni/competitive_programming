// Source : https://leetcode.com/problems/valid-anagram/
// Author : Hamza Mogni
// Date   : 2023-05-01

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

package main

import "fmt"

// isAnagram loops over first string and counts letters
// we do the counting in a hashmap. next we loop over
// second string: if we find a letter doesn't esist
// on hashmap or the count already reached 0 we
// return false. otherwise we decrement by 1
//
//	Complexity:
//		- Time: o(n)
//		- Space: o(1)
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	lettersCount := make(map[rune]int)

	for _, letter := range s {
		lettersCount[letter]++
	}

	for _, letter := range t {
		_, ok := lettersCount[letter]
		if !ok || lettersCount[letter] == 0 {
			return false
		}

		lettersCount[letter]--
	}

	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
	fmt.Println(isAnagram("cat", "rat"))
	fmt.Println(isAnagram("ab", "a"))
}
