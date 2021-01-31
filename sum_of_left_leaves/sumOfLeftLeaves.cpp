// 404. Sum of Left Leaves (leetcode)
//
// Find the sum of all left leaves in a given binary tree.
//
// Example:
//
//     3
//    / \
//   9  20
//     /  \
//    15   7
//
// There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

#include "sumOfLeftLeaves.h"


int sumOfLeftLeaves(TreeNode* root) {
    int sum = 0;

    if (root != nullptr){
        if (root->left != nullptr && root->left->left == nullptr && root->left->right == nullptr)
            sum += root->left->val;
        else
            sum += sumOfLeftLeaves(root->left);

        sum += sumOfLeftLeaves(root->right);
    }


    return sum;
}
