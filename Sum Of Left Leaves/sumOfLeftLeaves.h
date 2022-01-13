//
// Created by hmogni on 1/31/21.
//

#ifndef STUFF_SUMOFLEFTLEAVES_H
#define STUFF_SUMOFLEFTLEAVES_H

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
            : val(x), left(left), right(right) {}
};


int sumOfLeftLeaves(TreeNode* root);

#endif //STUFF_SUMOFLEFTLEAVES_H
