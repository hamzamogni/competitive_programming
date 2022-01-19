# Source : https://leetcode.com/problems/linked-list-cycle
# Author : Hamza Mogni
# Date   : 2022-01-20

#####################################################################################################
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by
# continuously following the next pointer. Internally, pos is used to denote the index of the node
# that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node
# (0-indexed).
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Constraints:
#
# 	The number of the nodes in the list is in the range [0, 10^4].
# 	-10^5 <= Node.val <= 10^5
# 	pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#####################################################################################################

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
