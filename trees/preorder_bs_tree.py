# [10,5, 1,7,40, 50]
from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class PreorderBST:
    def __init__(self):
        self.root = None

    def add(self, val: int):

        def __add(val: int, root: Node) -> Node:
            if not root:
                return Node(val)

            if val < root.val:
                root.left = __add(val, root.left)
            else:
                root.right = __add(val, root.right)

            return root

        self.root = __add(val, self.root)

    def print_inorder(self, root: Node):
        if root:
            yield from self.print_inorder(root.left)
            yield root.val
            yield from self.print_inorder(root.right)


INT_MIN = -float("inf")
INT_MAX = float("inf")


# Methods to get and set the value of static variable
# constructTreeUtil.preIndex for function construcTreeUtil()
def getPreIndex():
    return constructTreeUtil.preIndex


def incrementPreIndex():
    constructTreeUtil.preIndex += 1


# A recursive function to construct BST from pre[].
# preIndex is used to keep track of index in pre[]
def constructTreeUtil(pre, key, mini, maxi, size):
    # Base Case
    if getPreIndex() >= size:
        return None
    root = None

    # If current element of pre[] is in range, then
    # only it is part of current subtree
    if mini < key < maxi:

        # Allocate memory for root of this subtree
        # and increment constructTreeUtil.preIndex
        root = Node(key)
        incrementPreIndex()

        if getPreIndex() < size:
            # Construct the subtree under root
            # All nodes which are in range {min.. key} will
            # go in left subtree, and first such node will
            # be root of left subtree
            root.left = constructTreeUtil(pre,
                                          pre[getPreIndex()],
                                          mini, key, size)
        if getPreIndex() < size:
            # All nodes which are in range{key..max} will
            # go to right subtree, and first such node will
            # be root of right subtree
            root.right = constructTreeUtil(pre,
                                           pre[getPreIndex()],
                                           key, maxi, size)

    return root


# This is the main function to construct BST from given
# preorder traversal. This function mainly uses
# constructTreeUtil()


def constructTree(pre):
    constructTreeUtil.preIndex = 0
    size = len(pre)
    return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, size)


# A utility function to print inorder traversal of Binary Tree
def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)


if __name__ == '__main__':
    print("Pre-Order BST")
    bst = PreorderBST()
    for element in [10, 5, 1, 7, 40, 50]:
        bst.add(element)

    for val in bst.print_inorder(bst.root):
        print(val)

    # Driver code O(n)
    pre = [10, 5, 1, 7, 40, 50]

    # Function call
    root = constructTree(pre)

    print("Inorder traversal of the constructed tree: ")
    printInorder(root)
