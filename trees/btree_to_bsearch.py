from __future__ import annotations
from typing import List, Generator


class Node:
    def __init__(self, val):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.sorted_values: List[int] = []

    def set_inorder_vals(self, node: Node) -> List[Node]:
        def in_order_list(tree: Node) -> Generator[Node, None, None]:
            if not tree:
                return
            yield from in_order_list(tree.left)
            yield tree
            yield from in_order_list(tree.right)

        for node in in_order_list(node):
            self.sorted_values.append(node.val)

        self.sorted_values.sort(reverse=True)

    def build_btree(self, node: Node) -> Node:
        def __build_btree(node: Node) -> Node:
            if not node:
                return

            self.build_btree(node.left)
            node.val = self.sorted_values.pop()
            self.build_btree(node.right)
            return node

        self.root = __build_btree(node)

    def print_in_order(self):
        def __print_in_order(node: Node):
            if not node:
                return

            __print_in_order(node.left)
            print(node.val, end='->')
            __print_in_order(node.right)

        __print_in_order(self.root)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    bst = BinarySearchTree()
    bst.set_inorder_vals(root)
    bst.build_btree(root)
    bst.print_in_order()

    print()
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(4)
    bst = BinarySearchTree()
    bst.set_inorder_vals(root)
    bst.build_btree(root)
    bst.print_in_order()
