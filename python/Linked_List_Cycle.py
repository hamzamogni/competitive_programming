"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can 
be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time: o(n)
    # Space: o(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            We traverse our linked list and add visited
            nodes to a hashmap, if we find a node that
            already exists on the hash, it means that
            we have detected a cycle.
        """
        visited = set()

        current = head
        while current:
            if current in visited:
                return True

            visited.add(current)
            current = current.next

        return False


def array2List(array: List) -> ListNode:
    head = ListNode(array[0])

    current = head
    for digit in array[1:]:
        current.next = ListNode(digit)
        current = current.next

    return head


def printList(head: ListNode) -> None:
    current = head
    while current:
        print(current.val)
        current = current.next


s = Solution()
t1 = s.hasCycle(array2List([1]))
t2 = s.hasCycle(array2List([1, 2, 3, 1]))
