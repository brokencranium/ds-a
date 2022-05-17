from queue import PriorityQueue


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: Node
        """
        head = point = Node(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = Node(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


if __name__ == '__main__':
    l1 = Node(2, Node(4, Node(6, Node(10))))
    l2 = Node(5, Node(7, Node(1, Node(5))))

    sol = Solution().mergeKLists([l1, l2])
