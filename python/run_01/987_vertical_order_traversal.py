# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        col_table = defaultdict(list)
        min_col = max_col = 0
        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()

            if node:
                col_table[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        
        return [col_table[x] for x in range(min_col, max_col + 1)]