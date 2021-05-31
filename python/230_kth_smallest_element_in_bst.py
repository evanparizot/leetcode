# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(6)
a.left.left = TreeNode(2)
a.left.right = TreeNode(4)
a.right.right = TreeNode(7)

s = Solution()
s.kthSmallest(a, 5)