//
// Created by hmogni on 4/12/21.
//

#ifndef STUFF_ADD_TWO_NUMBERS_H
#define STUFF_ADD_TWO_NUMBERS_H

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}

    void printList();
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2);

#endif //STUFF_ADD_TWO_NUMBERS_H
