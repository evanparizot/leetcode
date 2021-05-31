# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, s):
        if s:
            return f'#{s.val} {self.traverse(s.left)} {self.traverse(s.right)}'
        return None
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        source = self.traverse(s)
        target = self.traverse(t)
        if target in source:
            return True
        return False
