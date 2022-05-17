from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float("-inf")

        def max_gain(node: Optional[TreeNode]):
            nonlocal max_val
            if not node:
                return 0

            max_gain(node.left)
            max_gain(node.right)

            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0

            new_path_val = node.val + left_val + right_val

            node.val = max(node.val,
                           node.val + left_val,
                           node.val + right_val
                           )

            max_val = max(node.val, max_val)
            max_val = max(max_val, new_path_val)

        max_gain(root)
        return max_val


if __name__ == '__main__':
    sol = Solution()
    # root = TreeNode(3)
    #
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(8)
    print(sol.maxPathSum(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.maxPathSum(root))
