# Construct tree from preorder and inorder traversal
# Inorder sequence: D B E A F C
# Preorder sequence: A B D E C F

from __future__ import annotations

from queue import Queue
from collections import deque

import math
from typing import List, Deque


class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode = None


class Node:
    def __init__(self, val: int, left: Node = None, right: Node = None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right


class Tree:

    def build_tree_in_pre(self, preorder: List[int], inorder: List[int]) -> Node:
        if not inorder or not preorder:
            return None

        root: Node = Node(preorder[0])
        mid: int = inorder.index(root.val)
        root.left: Node = self.build_tree_in_pre(preorder[1:mid + 1], inorder[:mid])
        root.right: Node = self.build_tree_in_pre(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def build_tree_in_level(self, levelorder: List[int], inorder: List[int]) -> Node:
        if not inorder or not levelorder:
            return None

        root: Node = Node(levelorder[0])

        mid = inorder.index(root.val)

        iols: List[int] = inorder[:mid + 1]
        iors: List[int] = inorder[mid + 1:]

        lols, lors = [], []

        for element in levelorder[1:]:
            elements = lols if element in iols else lors
            elements.append(element)

        root.left: Node = self.build_tree_in_level(lols, iols)
        root.right: Node = self.build_tree_in_level(lors, iors)
        return root

    def build_btree(self, node: Node) -> Node:

        pass

    def list_to_comp_btree(self, data: List[int]) -> Node:
        """
        10->12->15->25->30->36
        :param data:
        :return:
        """
        root: Node = None

        pipe: Deque = deque([], maxlen=len(data))

        for index, dat in enumerate(data):
            if not root:
                root = Node(dat)
                root.left = Node(data[1])
                root.right = Node(data[2])

                pipe.append(root.left)
                pipe.append(root.right)
                continue

            current: Node = pipe.popleft()

            try:
                current.left = Node(data[int(math.pow(2, index) + 1)])
                pipe.append(current.left)
            except IndexError as err:
                current.left = None

            try:
                current.right = Node(data[int(math.pow(2, index) + 2)])
                pipe.append(current.right)
            except IndexError as err:
                current.right = None

        return root

    def print_post_order_traversal(self, node: Node):
        current = node
        print(current.val)
        if current.left:
            self.print_post_order_traversal(current.left)

        if current.right:
            self.print_post_order_traversal(current.right)

    def list_to_node(self, inp: List[int]) -> Node:
        node: ListNode = None
        for val in inp:
            if not node:
                root = ListNode(val)
                node = root
                continue

            node.next = ListNode(val)
            node = node.next

        return root

    def traverse_linked_list(self, node: ListNode, steps: int) -> Node:
        for _ in range(steps):
            node = node.next

        if node:
            return Node(node.val)

        return None

    def linked_list_to_comp_btree(self, list_node: ListNode) -> Node:
        root: Node = None
        deq = deque([])
        while list_node:
            if not root:
                root = Node(list_node.val)
                root.left = self.traverse_linked_list(list_node, 1)
                root.right = self.traverse_linked_list(list_node, 2)

                deq.append(root.left)
                deq.append(root.right)

                list_node = list_node.next
                continue






        pass


if __name__ == '__main__':
    print("Build tree from list")
    tree = Tree()
    inp = [10, 2, 15, 25, 30, 36]
    list_nodes = tree.list_to_node(inp)
    print(list_nodes)

    # root = tree.list_to_comp_btree(inp)
    # tree.print_post_order_traversal(root)

    # print("Build tree from in-order and pre-order")
    # tree = Tree()
    # root = tree.build_tree_in_pre([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
    # print(root.val)
    # print(root.left.val)
    # print(root.right.val)
    # print(root.left.left.val)
    # print(root.left.right.val)
    # print(root.right.left.val)
    # print(root.right.right.val)
    #
    # print("Build tree from in-order and level-order")
    # tree = Tree()
    # root = tree.build_tree_in_level([20, 8, 22, 4, 12, 10, 14], [4, 8, 10, 12, 14, 20, 22])
    # print(root.val)
    # print(root.left.val)
    # print(root.right.val)
    # print(root.left.left.val)
    # print(root.left.right.val)
    # print(root.left.right.left.val)
    # print(root.left.right.right.val)
