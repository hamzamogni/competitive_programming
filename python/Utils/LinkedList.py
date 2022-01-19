from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def from_array(self, array: List) -> ListNode:
        self.head = ListNode(array[0])

        current = self.head
        for digit in array[1:]:
            current.next = ListNode(digit)
            current = current.next

        return self

    def __str__(self):
        current = self.head

        output = ""
        while current:
            output += str(current.val)
            output += " -> "
            current = current.next
        output += "None"
        return f'{output}'
