from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = -1, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class ReverseListKGroup:

    def reverse(self, head: ListNode, k=3):
        dummy = ListNode(-1)
        dummy.next = head

        current_pointer = head
        new_head = current_pointer

        counter = k

        for _ in range(k):
            if current_pointer and not hasattr(current_pointer, 'previous'):
                setattr(current_pointer, 'previous', None)

            new_head = current_pointer.next
            new_head.previous = current_pointer

        dummy = ListNode(-1)
        dummy.next = new_head
        for _ in range(k):
            if new_head.previous:
                new_head.next = new_head.previous
                delattr(new_head, 'previous')
                new_head = new_head.next
        return new_head


if __name__ == '__main__':
    Node = ListNode
    l1 = Node(2, Node(4, Node(6)))
    group = ReverseListKGroup()
    result = group.reverse(l1)
