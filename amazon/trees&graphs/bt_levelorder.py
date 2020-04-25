# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
from typing import List
class Solution():
    def levelOrder(self, root:TreeNode) -> List[List[int]]:
        levels, level = [], 0
        q = deque([root])
        while q:
            levels.append([])
            level_length = len(q)
            for _ in range(level_length):
                node = q.popleft()
                levels[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels