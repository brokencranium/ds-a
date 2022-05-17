from typing import Optional


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.sibling: Node = None


class MinHeap:
    def __init__(self):
        self.tree: Node = None
        self.prev_node: Node = None
        self.left_most: Node = None

    @staticmethod
    def heapify(tree: Node):
        while tree.parent:
            if tree.parent.val > tree.val:
                tree.val, tree.parent.val = tree.parent.val, tree.val
            else:
                break

    def push(self, node: Node):
        if not self.tree:
            self.tree = node
            return self

        node.parent = self.tree

        if self.tree.left is None:
            self.tree.left = node
            self.heapify(self.tree.left)

            if self.prev_node:
                self.prev_node.sibling = self.tree.left

            self.prev_node = self.tree.left

        elif self.tree.right is None:
            self.tree.right = node
            self.heapify(self.tree.right)
            self.tree.left.sibling = self.tree.right

            if not self.left_most:
                self.left_most = self.tree.left

            self.prev_node = self.tree.right

            if self.tree.sibling:
                self.tree = self.tree.sibling
            else:
                self.left_most.parent = self.tree
                self.tree = self.left_most
                self.left_most = None
                self.prev_node = None
        return self

    def get_root(self) -> Node:
        temp = self.tree
        while temp.parent:
            temp = temp.parent
        return temp

    def print_level_order_traversal(self):
        def level_order_traversal(node: Node, start_node: Optional[Node] = None):
            if not node:
                return

            print(node.val)

            if node.sibling:
                start_node = node if not start_node else start_node

                level_order_traversal(node.sibling, start_node)
            else:
                if start_node:
                    level_order_traversal(start_node.left, None)
                else:
                    level_order_traversal(node.left, start_node)

        level_order_traversal(self.get_root())


if __name__ == '__main__':
    heap = MinHeap()
    (heap
     .push(Node(5))
     .push(Node(10))
     .push(Node(15))
     .push(Node(20))
     .push(Node(100))
     .push(Node(25))
     .push(Node(30))
     .push(Node(35))
     .push(Node(40))
     .push(Node(45))
     )

    heap.print_level_order_traversal()
