# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from enum import Enum
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def get_lca(node, p, q):
            nonlocal lca

            # base case
            if not node:
                return False
            
            # left_result = traverse(node.left)
            # right_result = traverse(node.right)
            left_contains = get_lca(node.left, p, q)
            right_contains = get_lca(node.right, p, q)

            # if left_result and right_result: current is LCA
            if left_contains and right_contains:
                lca = node
            
            # If left branch or right branch has p or q and current node is p or q, 
            # current is lca
            elif node == p or node == q:
                if left_contains or right_contains:
                    lca = node

            return left_contains or right_contains or node == p or node == q

        lca = None
        get_lca(root, p, q)
        return lca

    def lowestCommonAncestor(self, root, p, q):
        States = enum(BOTH_PENDING = 2, LEFT_DONE = 1, BOTH_DONE = 0)

        # Iterative approach
        stack = [(root, States.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != States.BOTH_DONE:
                if parent_state == States.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) -1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                
                stack.pop()
                stack.append((parent_node, parent_state -1))

                if child_node:
                    stack.append((child_node, States.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) -1:
                    LCA_index -= 1
                stack.pop()
        return None


a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)
g = TreeNode(8)
h = TreeNode(7)
i = TreeNode(4)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

e.left = h
e.right = i

s = Solution()
s.lowestCommonAncestor(a, d, i)