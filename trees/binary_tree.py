from __future__ import annotations


class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None


class Tree:
    def __init__(self, node: Node):
        self.root: Node = node

    def add(self, node: Node):

        if self.root.left is None:
            self.root.left = node
        elif self.root.right is None:
            self.root.right = node
        else:
            temp = self.root
            self.root = self.root.left
            self.root.parent = temp
            self.root.left = node

        return self

    def print_pre_order(self, root: Node):
        if root:
            print(root.val, end=" ")

            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

    def print_post_order(self, root: Node):
        if root:
            self.print_post_order(root.left)
            self.print_post_order(root.right)

            print(root.val, end=" ")

    def print_in_order(self, root: Node):
        if root:
            self.print_in_order(root.left)
            print(root.val, end=" ")
            self.print_in_order(root.right)

    def print_in_order_stack(self, root: Node):
        stack = []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if not stack:
                    break

                current = stack.pop()
                print(current.val, end=" ")
                current = current.right

    def morris_traversal(self, root: Node):
        """
        Generator function for iterative inorder tree traversal
        Threaded binary tree
        """

        current = root

        while current is not None:

            if current.left is None:
                yield current.val
                current = current.right
            else:

                # Find the inorder
                # predecessor of current
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right

                if pre.right is None:

                    # Make current as right
                    # child of its inorder predecessor
                    pre.right = current
                    current = current.left

                else:
                    # Revert the changes made
                    # in the 'if' part to restore the
                    # original tree. i.e., fix
                    # the right child of predecessor
                    pre.right = None
                    yield current.val
                    current = current.right

    def print_morris_traversal(self, root):
        for v in self.morris_traversal(root):
            print(v, end=' ')

    def morris_traversal_v1(self, root: Node):
        current = root

        while current is not None:

            if current.left is None:
                yield current.val
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right

                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    yield current.val
                    current = current.right

    def print_morris_traversal_v1(self, root: Node):

        for val in self.morris_traversal_v1(root):
            print(val, end=" ->")


if __name__ == '__main__':
    # result = tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    root.left.right = Node(5)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)

    root.right.left = Node(6)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)

    root.right.right = Node(7)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    tree = Tree(root)
    # print("Pre-Order")
    # tree.print_pre_order(root)
    #
    # print("\nPost-Order")
    # tree.print_post_order(root)
    #
    # print("\nPrint-In-Order-Recursive")
    # tree.print_in_order(root)
    #
    # print("\nPrint-In-Order-Iterative")
    # tree.print_in_order_stack(root)

    print("\nPrint-In-Order-Morris")
    tree.print_morris_traversal(root)
    print()
    tree.print_morris_traversal_v1(root)
