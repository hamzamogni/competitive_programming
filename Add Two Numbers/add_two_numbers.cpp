//
// Created by hmogni on 4/12/21.
//
#include <iostream>

#include "add_two_numbers.h"

using namespace std;

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
{
    auto* sum = new ListNode(0);
    ListNode* a(l1);
    ListNode* b(l2);

    while (a && b)
    {
        sum->next = new ListNode(a->val + b->val, nullptr);
        a = a->next;
        b = b->next;
    }

    sum->next->printList();

    return sum;
}

void ListNode::printList()
{
    ListNode* current(this);

    while(current)
    {
        cout << current->val << "-->";
        current = current->next;
    }
    cout << "nullptr" << endl;
}