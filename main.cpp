#include <iostream>
#include <vector>

#include "sum_of_left_leaves/sumOfLeftLeaves.h"


using namespace std;

int main() {
    TreeNode tree(3);
    tree.left = new TreeNode(9);
    tree.right = new TreeNode(20);

    tree.right->left = new TreeNode(15);
    tree.right->right = new TreeNode(7);

    cout << sumOfLeftLeaves(&tree) << endl;
}