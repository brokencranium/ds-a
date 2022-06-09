from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flat(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Handle the null scenario
            if not node:
                return None

            # For a leaf node, we simply return the
            # node as is.
            if not node.left and not node.right:
                return node

            # Recursively flatten the left subtree
            left_tail = flat(node.left)

            # Recursively flatten the right subtree
            right_tail = flat(node.right)

            # If there was a left subtree, we shuffle the connections
            # around so that there is nothing on the left side
            # anymore.
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # We need to return the "rightmost" node after we are
            # done wiring the new connections.
            return right_tail if right_tail else left_tail

        flat(root)


if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6)))
    sol.flatten(root)
    print(root)
