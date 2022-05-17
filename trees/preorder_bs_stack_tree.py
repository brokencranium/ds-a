from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class PreorderBSTStack:
    def __init__(self):
        self.root = None
        self.stack = []

    def add(self, values: List):
        self.root: Node = Node(values[0])
        stack = [self.root]

        for index in range(1, len(values), 1):
            if values[index] < stack[-1].val:
                stack[-1].left = Node(values[index])
                stack.append(stack[-1].left)
            else:
                while stack:  # TODO
                    if values[index] > stack[-1].val:
                        temp = stack.pop()
                    else:
                        temp.right = Node(values[index])
                        stack.append(temp.right)
                        break

                if not stack:
                    temp.right = Node(values[index])
                    stack.append(temp.right)

    def print_inorder(self, root: Node):
        if root:
            yield from self.print_inorder(root.left)
            yield root.val
            yield from self.print_inorder(root.right)


if __name__ == '__main__':

    print("Pre-Order BST Stack")
    bst_stack = PreorderBSTStack()
    # bst_stack.add([10, 5, 1, 7, 40, 50])
    bst_stack.add([20, 10, 5, 1, 7, 15, 22, 30, 25, 35, 32, 40])
    for val in bst_stack.print_inorder(bst_stack.root):
        print(val)
