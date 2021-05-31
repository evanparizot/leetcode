class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def next(self) -> int:
        topmost = self.stack.pop()

        if topmost.right:
            self._leftmost_inorder(topmost.right)
        return topmost.val