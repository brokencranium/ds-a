class Node:
    def __init__(self, val: int):
        self.next: Node = None
        self.val = val


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def push(self, new_node: Node):
        if self.head is None:
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
        return self

    def append(self, new_node: Node):

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self

    def delete(self, node: Node):
        curr_node: Node = self.head
        prev_node: Node = None
        while curr_node.next:
            if self.head == node:
                self.head == node.next
                break
            elif curr_node == node:
                prev_node.next = curr_node.next
                break
            else:
                prev_node = curr_node
                curr_node = curr_node.next

        if node == self.tail and prev_node.next is not None:
            self.tail = prev_node.next
        elif node == self.tail:
            self.tail = prev_node

    @staticmethod
    def insert_after(prev_node: Node, new_node: Node):
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_node(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val)
            curr_node = curr_node.next
        print()

    def reverse(self):
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            nxt = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt

        self.head = prev_node

    def remove_dupes(self):
        curr_node = self.head
        unique_vals = set()

        while curr_node is not None:
            if curr_node.val in unique_vals:
                nxt = curr_node.next

                if nxt is not None:
                    curr_node = nxt.next
                else:
                    curr_node = None
            else:
                unique_vals.add(curr_node.val)
                curr_node = curr_node.next


if __name__ == '__main__':
    linked_list = (LinkedList()
                   .push(Node(8))
                   .push(Node(4))
                   )
    # linked_list.print_node()
    node_12 = Node(12)
    (linked_list
     .append(Node(10))
     .append(node_12)
     .append(Node(14))
     )

    # linked_list.print_node()

    (linked_list.insert_after(node_12, Node(13)))
    linked_list.print_node()

    linked_list.delete(node_12)
    linked_list.print_node()

    linked_list.reverse()
    linked_list.print_node()
