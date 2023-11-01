from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def maxSumPath(self, root: TreeNode) -> int:

        def traverse(node: TreeNode) -> None:
            # Base Case
            # If node is none, return 0

            # Traverse left, get sum. If sum < 0, just take zero
            # Traverse right, get sum. If sum < 0, just take zero

            # Determine if current + left + right > running max. If so update

            # Return current.val + max(left, right)

    
