from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next: Optional[Node] = next


class MergeLists:
    def merge_iter(self, list1: Node, list2: Node) -> Optional[Node]:
        root = Node(-1)

        prev = root
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next

            prev = prev.next

        prev.next = list1 or list2

        return root.next

    def merge_recur(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.merge_recur(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_recur(l1, l2.next)
            return l2


if __name__ == '__main__':
    l1 = Node(2, Node(4, Node(6, Node(10))))
    l2 = Node(5, Node(7, Node(9, Node(11))))
    merge = MergeLists()
    # result = merge.merge_iter(l1, l2)
    result = merge.merge_recur(l1, l2)
    print(result)
