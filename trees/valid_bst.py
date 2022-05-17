from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous_val = float("-inf")

        def traverse_bst(root: Optional[TreeNode]) -> Optional[bool]:
            nonlocal previous_val
            if not root:
                return True

            result = traverse_bst(root.left)
            current_val = root.val

            if current_val <= previous_val or not result:
                return False

            previous_val = current_val

            return traverse_bst(root.right)

        return traverse_bst(root)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(3)
    sol = Solution()
    print(sol.isValidBST(root))
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)
    # root.right.left.right = Node(8)
    # root.right.right.right = Node(9)
