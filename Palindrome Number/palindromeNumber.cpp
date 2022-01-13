#include <iostream>
#include <math.h>

using namespace std;

bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    } else if (x == 0) {
        return true;
    }

    int length = (int)log10(x) + 1;
    cout << length;

    return true;
}
