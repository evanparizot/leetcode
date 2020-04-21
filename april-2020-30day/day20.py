from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#         Return the root node of a binary search tree that matches the given preorder traversal.
      # (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and 
      # any descendant of node.right has a value > node.val. 
      #  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

      # Input: [8,5,1,7,10,12]
      # Output: [8,5,10,1,7,null,12]


      # NOTE preorder length will be between 1 <= 100
      root = TreeNode(preorder[0]) # Add root node

      if len(preorder) <= 1:
        return root

      # Contruct tree here
      for i in range(1, len(preorder)):
        
        current = root
        while current is not None:
          # Need to check if current preorder element is less than current node
          if preorder[i] < current.val:
            if current.left is None:
              current.left = TreeNode(preorder[i])
              current = None
            else:
              current = current.left

          elif preorder[i] > current.val:
            if current.right is None:
              current.right = TreeNode(preorder[i])
              current = None
            else:
              current = current.right

      return root

s = Solution()
s.bstFromPreorder([8,5,1,7,10,12])