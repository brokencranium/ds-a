class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Node = None


class CircularLinkedList:
    def __init__(self):
        self.head: Node = None

    def push(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            curr_node = self.head
            self.head = node
            self.head.next = curr_node
        return self

    def print_circular_list(self, start: Node):

        print(start.val)
        while self.head != start:
            print(self.head.val)
            self.head = self.head.next


if __name__ == '__main__':
    cll = CircularLinkedList()
    start_node = Node(8)
    nodes = (cll
             .push(start_node)
             .push(Node(6))
             .push(Node(4))
             .push(Node(2))
             )
    nodes.print_circular_list(start_node)
