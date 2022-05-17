from __future__ import annotations
from typing import List

import math


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None


class BalancedBtree():
    def __init__(self):
        self.root: Node = None

    def build_tree_v1(self, values: List[int]) -> Node:

        def build_tree(root: Node, values: List[int]) -> Node:
            if not values:
                return

            mid = len(values) // 2
            current = Node(values[mid])

            if len(values) > 1:
                current.left = build_tree(current, values[:mid])
                current.right = build_tree(current, values[mid + 1:])

            return current

        mid = len(values) // 2
        self.root = Node(values[mid])
        self.root.left = build_tree(self.root, values[:mid])
        self.root.right = build_tree(self.root, values[mid + 1:])

    def print_in_order(self, node: Node):
        if not node:
            return

        self.print_in_order(node.left)
        print(node.val)
        self.print_in_order(node.right)


if __name__ == '__main__':
    # test1 = [1, 2, 3]
    test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    bb_tree = BalancedBtree()
    bb_tree.build_tree_v1(test1)
    bb_tree.print_in_order(bb_tree.root)
