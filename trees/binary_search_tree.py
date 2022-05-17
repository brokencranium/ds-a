from __future__ import annotations
from typing import Optional, Generator
import timeit


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def __insert(self, root: Node, val: int) -> BinarySearchTree:
        if not root:
            return Node(val)

        if val < root.val:
            root.left = self.__insert(root.left, val)
        elif val > root.val:
            root.right = self.__insert(root.right, val)

        return root

    def insert(self, val):
        self.root = self.__insert(self.root, val)

    def search(self, val: int, root: Optional[Node] = None, parent: Optional[Node] = None) -> Optional[Node]:
        if not root or val == root.val:
            return root, parent
        elif val < root.val:
            return self.search(val, root.left, root)
        else:
            return self.search(val, root.right, root)

    def in_order_node(self, root: Node, parent: Node = None):
        if root and root.left:
            self.in_order_node(root.left, root)
        else:
            return root, parent

    def delete(self, val):
        current_node, parent_current_node = self.search(val, self.root)

        if current_node:

            if current_node.left and current_node.right:
                in_order_node, parent_node = self.in_order_node(current_node.right)
                current_node.val = in_order_node.val
                parent_node.left = None

            elif current_node.right:
                if parent_current_node.right.val == val:
                    parent_current_node.right = current_node.right
                else:
                    parent_current_node.left = current_node.right

                parent_current_node.right = current_node.right

            elif current_node.left:
                parent_current_node.left = current_node.left
            elif parent_current_node:
                if parent_current_node.right.val == val:
                    parent_current_node.right = None
                else:
                    parent_current_node.left = None

    def in_order_traversal(self, root: Node) -> Generator[int, None, None]:
        # 5.029200000000039e-05
        if root:
            yield from self.in_order_traversal(root.left)
            yield root.val
            yield from self.in_order_traversal(root.right)

    @staticmethod
    def outer():
        # 5.275000000000071e-05
        def in_order(root: Node) -> Generator[int, None, None]:
            if root:
                yield from in_order(root.left)
                yield root.val
                yield from in_order(root.right)

        return in_order

    def in_order_traversal_v1(self, root: Node) -> Generator[int, None, None]:
        # 4.5083000000001316e-05
        if root:
            self.in_order_traversal_v1(root.left)
            print(root.val, end="->")
            self.in_order_traversal_v1(root.right)

    def print_in_order_traversal(self):
        # self.in_order_traversal_v1(self.root)
        for value in self.in_order_traversal(self.root):
            print(value, end="->")

    def print_in_order_traversal_v1(self):
        # self.in_order_traversal_v1(self.root)
        out = self.outer()

        for val in out(self.root):
            print(val, end="->")


if __name__ == '__main__':
    bs = BinarySearchTree()
    bs.insert(50)
    bs.insert(30)
    bs.insert(20)
    bs.insert(40)
    bs.insert(70)
    bs.insert(60)
    bs.insert(80)
    bs.insert(25)
    bs.insert(85)
    bs.insert(75)
    bs.print_in_order_traversal_v1()

    print()
    bs.delete(75)
    bs.print_in_order_traversal_v1()

    print()
    bs.delete(20)
    bs.print_in_order_traversal_v1()

#     print(timeit.timeit('''
# bs = BinarySearchTree()
# bs.insert(50)
# bs.insert(30)
# bs.insert(20)
# bs.insert(40)
# bs.insert(70)
# bs.insert(60)
# bs.insert(80)
# bs.print_in_order_traversal_v1()
#     ''', number=1, globals=globals()))
