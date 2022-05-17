class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        node = ListNode(x)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, x):
        if self.head is None:
            return
        if self.head.val == x:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        if self.tail.val == x:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            return

        curr = self.head
        while curr is not None:
            if curr.val == x:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return
            curr = curr.next

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    def reverse(self):
        curr = self.head
        while curr is not None:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            curr = curr.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def reverse_recursive(self):
        self.reverse_recursive_helper(self.head)

    def reverse_recursive_helper(self, node):
        if node is None or node.next is None:
            self.head = node
            return
        self.reverse_recursive_helper(node.next)
        node.next.prev = node
        node.next = None
        node.prev = node.next

