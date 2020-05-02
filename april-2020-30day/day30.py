# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            return False

        def isleaf(node) -> bool:
            return not node.left and not node.right

        def traverse(node, index):
            if not node:
                return False
            if index > len(arr):
                return False

            if arr[index] != node.val:
                return False

            if arr[index] == node.val and isleaf(node):
                return True

            return traverse(node.left, index + 1) or traverse(node.right, index + 1)

        return traverse(root, 0)

a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(0)
d = TreeNode(0)
e = TreeNode(1)
f = TreeNode(0)
g = TreeNode(1)
h = TreeNode(0)
i = TreeNode(0)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

d.right = g

e.left = h
e.right = i

s = Solution()
print(s.isValidSequence(a, [0,1,0,7]))
