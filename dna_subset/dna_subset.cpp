// 187. Repeated DNA Sequences (leetcode)
//
// All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T',
// for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
// repeated sequences within the DNA.
//
//Write a function to find all the 10-letter-long sequences (substrings)
// that occur more than once in a DNA molecule.
//
//
//
//Example 1:
//
//Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
//Output: ["AAAAACCCCC","CCCCCAAAAA"]

#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> findRepeatedDnaSequences(string const& s) {
  vector<string> returned;
  map<string, int> subsets_count;
  for (int i = 0; i+9 < s.length(); i++) {
      string current = s.substr(i, 10);
      subsets_count[current]++;
      if (subsets_count[current] == 2) 
        returned.push_back(current);
  }
  return returned;
}
