from __future__ import annotations
from typing import Optional, OrderedDict


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class VerticalBinaryTree:
    def __init__(self, tree: Node):
        self.tree = tree
        self.weights: dict = {}

    def calculate_distance(self, parent: Node, distance: int = 0, depth: int = 0):
        if not parent:
            return

        if distances := self.weights.get(distance):
            if vals := distances.get(depth):
                vals.append(parent.val)
            else:
                distances[depth] = [parent.val]

        else:
            self.weights[distance] = {depth: [parent.val]}

        self.calculate_distance(parent.left, distance - 1, depth + 1)
        self.calculate_distance(parent.right, distance + 1, depth + 1)

    def print_vertical_tree(self):
        for key, vals in sorted(self.weights.items()):
            print("key", end=" : ")
            for k, v in sorted(vals.items()):
                print(*v, end="->")

            print()

if __name__ == '__main__':
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)
    # root.right.left.right = Node(8)
    # root.right.right.right = Node(9)

    root = Node(1);
    root.left = Node(2);
    root.right = Node(3);
    root.left.left = Node(4);
    root.left.right = Node(5);
    root.right.left = Node(6);
    root.right.right = Node(7);
    root.right.left.right = Node(8);
    root.right.right.right = Node(9);
    root.right.right.left = Node(10);
    root.right.right.left.right = Node(11);
    root.right.right.left.right.right = Node(12);

    vbt = VerticalBinaryTree(root)
    vbt.calculate_distance(root)
    vbt.print_vertical_tree()
    # print(vbt.weights)
