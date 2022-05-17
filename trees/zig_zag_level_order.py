from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = [[root.val]]
        queue: List[(TreeNode, int)] = [(root, 0)]

        def level_order():
            parent, level = queue.pop(0)
            level += 1
            if not parent:
                return

            pair = []
            if parent.left:
                pair.append(parent.left.val)

            if parent.right:
                pair.append(parent.right.val)

            if level % 2 == 0 and level > 1:
                zig_zag = 1
            else:
                zig_zag = -1

            if pair:
                result.append(pair[::zig_zag])

            queue.append((parent.left, level))
            queue.append((parent.right, level))
            level_order()

        level_order()
        return result


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(8)
    print(sol.zigzagLevelOrder(root))
