from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def from_array(array: List) -> ListNode:
        self.head = ListNode(array[0])

        current = head
        for digit in array[1:]:
            current.next = ListNode(digit)
            current = current.next

        return self.head

    def __str__():
        current = self.head

        while current:
            print(current.val, end="")
            print(" -> ")
            current = current.next
