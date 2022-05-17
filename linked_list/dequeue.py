from __future__ import annotations


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.prev: Node = None
        self.nxt: Node = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Node = None
        self.last: Node = None

    def add_bottom(self, val: int) -> DoubleLinkedList:
        node = Node(val)
        self.last.nxt = node
        self.last = node

        return self

    def pop(self) -> DoubleLinkedList:
        self.head = self.head.nxt
        return self

    def dequeue(self) -> DoubleLinkedList:
        # self.tail
        self.last = self.last.prev
        self.last.nxt = None
        return self

    def push(self, val: int) -> DoubleLinkedList:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.head.prev = node
            node.nxt = self.head
            self.head = node

        return self

    def __repr__(self):
        curr_node = self.head
        out = str(curr_node.val)
        while curr_node.nxt is not None:
            curr_node = curr_node.nxt
            out += f'-> {curr_node.val}'

        return out


if __name__ == '__main__':
    dbl_list = (DoubleLinkedList()
                .push(10)
                .push(9)
                .push(8)
                .push(7)
                .push(6)
                .pop()
                .dequeue()

                )
    print(dbl_list)
