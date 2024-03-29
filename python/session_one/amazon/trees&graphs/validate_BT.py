# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def traverse(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not traverse(node.right, val, upper):
                return False
            if not traverse(node.left, lower, val):
                return False
            return True
        return traverse(root)
        
    def isValidBST2(self, root:TreeNode) -> bool:
        if not root: return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    # L -> Root -> R

    def isValidBST3(self, root: TreeNode) -> bool:
        # In order traversal
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                # traverse left all the way
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True