# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverse_list(head: Optional[ListNode]) -> str:
    result = ""
    while head:
        result += str(head.val)
        head = head.next

    return result[::-1]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_1 = int(traverse_list(l1))
        result_2 = int(traverse_list(l2))
        result = str(result_1 + result_2)

        prev_node = None
        curr_node = None
        for val in result:
            curr_node = ListNode(val, prev_node)
            prev_node = curr_node
        return curr_node


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
    result = Solution().addTwoNumbers(l1, l2)
    print(traverse_list(result))
