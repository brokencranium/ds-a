# The thief has found a new place for his thievery.
# There is only one entrance to this area, called the "root."
# Besides the root, each house has one and only one parent house.
# After a tour, the smart thief realized that "all houses in this place forms a binary tree".
# It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.

import collections


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        self.memo[root] = max(root.val + self.rob(root.left) + self.rob(root.right),
                              self.rob(root.left) + self.rob(root.right))
        return self.memo[root]

    def rob_recursive(self, root):
        if not root:
            return 0
        left = self.rob_recursive(root.left)
        right = self.rob_recursive(root.right)
        return max(root.val + left + right, left + right)

    def rob_iterative(self, root):
        if not root:
            return 0
        prev_left = 0
        prev_right = 0
        curr_left = 0
        curr_right = 0
        curr = 0
        while root:
            curr_left = max(prev_left + root.val, curr_left)
            curr_right = max(prev_right + root.val, curr_right)
            curr = max(curr_left, curr_right)
            prev_left = curr_left
            prev_right = curr_right
            root = root.left
        return curr

    def rob_recursive_memo(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        left = self.rob_recursive_memo(root.left)
        right = self.rob_recursive_memo(root.right)
        self.memo[root] = max(root.val + left + right, left + right)
        return self.memo[root]

    def rob_iterative_memo(self, root):
        if not root:
            return 0
        prev_left = 0
        prev_right = 0
        curr_left = 0

        while root:
            curr_left = max(prev_left + root.val, curr_left)
            prev_left = curr_left
            root = root.left
        return curr_left

    def rob_recursive_memo_with_cache(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        left = self.rob_recursive_memo_with_cache(root.left)
        right = self.rob_recursive_memo_with_cache(root.right)
        self.memo[root] = max(root.val + left + right, left + right)
        return self.memo[root]

    def rob_iterative_memo_with_cache(self, root):
        if not root:
            return 0
        prev_left = 0
        prev_right = 0
        curr_left = 0
        curr_right = 0
        curr = 0
        while root:
            curr_left = max(prev_left + root.val, curr_left)
            curr_right = max(prev_right + root.val, curr_right)
            curr = max(curr_left, curr_right)
            prev_left = curr_left
            prev_right = curr_right
            root = root.left
        return curr

    def rob_recursive_memo_with_cache_with_hashmap(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        left = self.rob_recursive_memo_with_cache_with_hashmap(root.left)
        right = self.rob_recursive_memo_with_cache_with_hashmap(root.right)
        self.memo[root] = max(root.val + left + right, left + right)
        return self.memo[root]

    def rob_iterative_memo_with_cache_with_hashmap(self, root):
        if not root:
            return 0
        prev_left = 0
        prev_right = 0
        curr_left = 0
        curr_right = 0
        curr = 0
        while root:
            curr_left = max(prev_left + root.val, curr_left)
            curr_right = max(prev_right + root.val, curr_right)
            curr = max(curr_left, curr_right)
            prev_left = curr_left
            prev_right = curr_right
            root = root.left
        return curr

    def rob_recursive_memo_with_cache_with_hashmap_with_dict(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        left = self.rob_recursive_memo_with_cache_with_hashmap_with_dict(root.left)
        right = self.rob_recursive_memo_with_cache_with_hashmap_with_dict(root.right)
        self.memo[root] = max(root.val + left + right, left + right)
        return self.memo[root]

    def rob_iterative_memo_with_cache_with_hashmap_with_dict(self, root):
        if not root:
            return 0
        prev_left = 0
        prev_right = 0
        curr_left = 0
        curr_right = 0
        curr = 0
        while root:
            curr_left = max(prev_left + root.val, curr_left)
            curr_right = max(prev_right + root.val, curr_right)
            curr = max(curr_left, curr_right)
            prev_left = curr_left
            prev_right = curr_right
            root = root.left
        return curr

    def rob_recursive_memo_with_cache_with_hashmap_with_dict_with_defaultdict(self, root):
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        left = self.rob_recursive_memo_with_cache_with_hashmap_with_dict_with_defaultdict(root.left)
        right = self.rob_recursive_memo_with_cache_with_hashmap_with_dict_with_defaultdict(root.right)
        self.memo[root] = max(root.val + left + right, left + right)
        return self.memo[root]

    def rob_dynamic_programming(self, root):
        if not root:
            return 0
        memo = {}
        return self.rob_recursive_memo_with_cache_with_hashmap_with_dict_with_defaultdict(root, memo)


#   Read the current node
#   Store the current node and sum(child nodes)


if __name__ == "__main__":
    TreeNode = collections.namedtuple("TreeNode", ["val", "left", "right"])
    root = TreeNode(3, TreeNode(2, TreeNode(3, None, TreeNode(3, None, TreeNode(1))), TreeNode(3, None, TreeNode(1))),
                    TreeNode(3, None, TreeNode(1)))
    print(Solution().rob_recursive_memo(root))

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(Solution().rob_recursive_memo(root))
    print(Solution().rob_iterative_memo(root))
    print(Solution().rob(root))
    print(Solution().rob_recursive(root))
    print(Solution().rob_iterative(root))
    print(Solution().rob_recursive_memo(root))
    print(Solution().rob_iterative_memo(root))
