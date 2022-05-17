class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.parent: Node = None
        self.child: Node = None
        self.sibling: Node = None
        self.degree: int = None


class Heap:
    def __int__(self):
        self.heap = None

        # if not self.heap:
        #     self.heap = node
        #     return

    def push(self, heap:Node, node:Node):
        if not node:
            return

        if heap.val < node.val:
            self.push(heap.left)
        else:
            self.push(heap.right)





        if self.heap.left is None:
            self.heap.left = Node(val)
        elif self.heap.right is None:
            self.heap.right = Node(val)
        else

    def pop(self):

        pass

    def peek(self):
        pass

    def decrease(self):
        pass

    def heapify(self):
        pass


class BinomialHeap(Heap):
    def __init__(self):
        pass
