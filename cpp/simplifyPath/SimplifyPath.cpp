// Source : https://leetcode.com/problems/simplify-path
// Author : Hamza Mogni
// Date   : 2022-03-15

/***************************************************************************************************** 
 *
 * Given a string path, which is an absolute path (starting with a slash '/') to a file or directory 
 * in a Unix-style file system, convert it to the simplified canonical path.
 * 
 * In a Unix-style file system, a period '.' refers to the current directory, a double period '..' 
 * refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as 
 * a single slash '/'. For this problem, any other format of periods such as '...' are treated as 
 * file/directory names.
 * 
 * The canonical path should have the following format:
 * 
 * 	The path starts with a single slash '/'.
 * 	Any two directories are separated by a single slash '/'.
 * 	The path does not end with a trailing '/'.
 * 	The path only contains the directories on the path from the root directory to the target 
 * file or directory (i.e., no period '.' or double period '..')
 * 
 * Return the simplified canonical path.
 * 
 * Example 1:
 * 
 * Input: path = "/home/"
 * Output: "/home"
 * Explanation: Note that there is no trailing slash after the last directory name.
 * 
 * Example 2:
 * 
 * Input: path = "/../"
 * Output: "/"
 * Explanation: Going one level up from the root directory is a no-op, as the root level is the 
 * highest level you can go.
 * 
 * Example 3:
 * 
 * Input: path = "/home//foo/"
 * Output: "/home/foo"
 * Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 * 
 * Constraints:
 * 
 * 	1 <= path.length <= 3000
 * 	path consists of English letters, digits, period '.', slash '/' or '_'.
 * 	path is a valid absolute Unix path.
 ******************************************************************************************************/
/***************************************************************************************************** 
 *
 * Given a string path, which is an absolute path (starting with a slash '/') to a file or directory 
 * in a Unix-style file system, convert it to the simplified canonical path.
 * 
 * In a Unix-style file system, a period '.' refers to the current directory, a double period '..' 
 * refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as 
 * a single slash '/'. For this problem, any other format of periods such as '...' are treated as 
 * file/directory names.
 * 
 * The canonical path should have the following format:
 * 
 * 	The path starts with a single slash '/'.
 * 	Any two directories are separated by a single slash '/'.
 * 	The path does not end with a trailing '/'.
 * 	The path only contains the directories on the path from the root directory to the target 
 * file or directory (i.e., no period '.' or double period '..')
 * 
 * Return the simplified canonical path.
 * 
 * Example 1:
 * 
 * Input: path = "/home/"
 * Output: "/home"
 * Explanation: Note that there is no trailing slash after the last directory name.
 * 
 * Example 2:
 * 
 * Input: path = "/../"
 * Output: "/"
 * Explanation: Going one level up from the root directory is a no-op, as the root level is the 
 * highest level you can go.
 * 
 * Example 3:
 * 
 * Input: path = "/home//foo/"
 * Output: "/home/foo"
 * Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 * 
 * Constraints:
 * 
 * 	1 <= path.length <= 3000
 * 	path consists of English letters, digits, period '.', slash '/' or '_'.
 * 	path is a valid absolute Unix path.
 ******************************************************************************************************/

#include <iostream>
#include <vector>
#include <string>
#include <assert.h>

using namespace std;

class Solution
{
public:
    /**
     *  We will first split our string by the "/" character
     *  then we will resolve our path and return it.
     * 
     *  Complexity:
     *      Time: o(n)
     *      Space: o(n)
     **/
    string simplifyPath(string path) {
        vector<string> splitInput, 
                        parsedParts;

        string tmp = "",
                final = "";

        path += "/";

        // We split input path by the "/" character
        for (char chr: path) {
            if (chr == '/') {
                splitInput.push_back(tmp);
                tmp = "";
                continue;
            }
            tmp += chr;
        }

        // we resolve the path according to rules
        for (string part: splitInput) {
            if (part == "." || part == "") {
                continue;
            } else if (part == "..") {
                if (!parsedParts.size()) {
                    continue;
                }
                parsedParts.pop_back();
            } else {
                parsedParts.push_back(part);
            }
        }

        // if we end up with empty path
        // then we are at the root of
        // our filesystem
        if (!parsedParts.size()) {
            return "/";
        }

        // we assemble the resolved path
        // and return it
        for (string part: parsedParts) {
            final += "/" + part;
        }
        return final;
    }
};

int main()
{
    Solution s = Solution();
    assert(s.simplifyPath("/home/") == "/home");
    assert(s.simplifyPath("/../") == "/");
    assert(s.simplifyPath("/home//foo") == "/home/foo");
    return 0;
}