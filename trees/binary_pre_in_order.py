from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def build_tree(self, pre_order: List[int], inorder: List[int]) -> Node:
        if not pre_order or not inorder:
            return None

        root = Node(pre_order[0])
        mid_point = inorder.index(pre_order[0])
        root.left = self.build_tree(pre_order[1:mid_point + 1], inorder[:mid_point])
        root.right = self.build_tree(pre_order[mid_point + 1:], inorder[mid_point + 1:])

        return root

    def print_pre_order(self, root):
        if not root:
            return None

        print(root.val)
        self.print_pre_order(root.left)
        self.print_pre_order(root.right)


if __name__ == '__main__':
    bin = BinaryTree()
    pre_order = ["A", "B", "D", "E", "C", "F"]
    in_order = ["D", "B", "E", "A", "F", "C"]
    root = bin.build_tree(pre_order, in_order)
    bin.print_pre_order(root)
