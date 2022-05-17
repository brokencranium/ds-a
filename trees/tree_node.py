class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val) + str(self.left) + str(self.right)


if __name__ == '__main__':
    root = TreeNode(1, None, None)
    root.left = TreeNode(2, None, None)
    root.right = TreeNode(3, None, None)

    for a in root.__dict__:
        print(a, root.__dict__[a])
