#include <vector>
#include <iostream>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode *
listFromArray(std::vector<int> input)
{
    ListNode *head = new ListNode(input[0]);

    ListNode *current = head;
    for (int i = 1; i < input.size(); i++)
    {
        current->next = new ListNode(input[i]);
        current = current->next;
    }

    return head;
}

void printList(ListNode *head)
{
    ListNode *current = head;

    while (current)
    {
        std::cout << current->val << " --> ";
        current = current->next;
    }
    std::cout << "NULL" << std::endl;
}