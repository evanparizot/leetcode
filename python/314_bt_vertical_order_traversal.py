# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        """
        T = O(nlngn) -> n being number of nodes
            - BFS takes O(n) time
            - Sorting takes O(nlgn)
        S = O(n) 
        """
        coltable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node is not None:
                coltable[col].append(node.val)

                queue.append((node.left, col -1))
                queue.append((node.right, col + 1))
        return [coltable[x] for x in sorted(coltable.keys())]

    def verticalOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        T = O(N)
            - No longer sorting
        S = O(N)
        """
        if not root:
            return []
        
        coltable = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node:
                coltable[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        return [coltable[x] for x in range(min_col, max_col +1)]