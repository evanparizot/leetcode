# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # Do a dfs, annotating parent


    def distanceK2(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        nodes = [(target, 0)]
        visited = set()
        while len(nodes):
            new_nodes = []
            for node, dist in nodes:
                visited.add(node.val)
                if dist == K:
                    return [target.val for target, dis in nodes]
                if node.right and node.right.val not in visited:
                    new_nodes.append((node.right, dist + 1))
                if node.left and node.left.val not in visited:
                    new_nodes.append((node.left, dist + 1))
                if node.par and node.par.val not in visited:
                    new_nodes.append((node.par, dist + 1))
            nodes = new_nodes
        return []