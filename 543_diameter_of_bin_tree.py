# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest = 0
        self.postDFS(root, longest)
        return longest
        
    def postDFS(self, node, longest):
        
        # Base Case
        if not node:
            return 0
        
        left_length = self.postDFS(node.left, longest)
        right_length = self.postDFS(node.right, longest)
        
        longest = max(longest, left_length + right_length)
        
        return max(left_length, right_length) + 1