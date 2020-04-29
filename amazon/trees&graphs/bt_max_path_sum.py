# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self):
    #     self.answer = float('-inf')
    
    # def _max_sum(self, root: TreeNode) -> int:
    #     if not root:
    #         return float('-inf')
    #     left_sum = self._max_sum(root.left)
    #     right_sum = self._max_sum(root.right)
        
    #     max_between_below = max(root.val, left_sum, right_sum, root.val + left_sum, root.val + right_sum)
    #     self.answer = max(self.answer, max_between_below, root.val + left_sum + right_sum)
        
    #     return max_between_below
    
    # def maxPathSum(self, root: TreeNode) -> int:
    #     self._max_sum(root)
    #     return self.answer

    def maxPathSum(self, root: TreeNode) -> int:
        def max_sum(node: TreeNode):
            nonlocal answer
            if not node:
                return 0
            
            left_sum = max(max_sum(node.left), 0)
            right_sum = max(max_sum(node.right), 0)

            newpath = node.val + left_sum + right_sum

            answer = max(answer, newpath)

            return node.val + max(left_sum, right_sum)
        
        answer = float('-inf')
        max_sum(root)
        return answer

#     5
#    / \
#   8   20
#      /  \
#     15   45
#    /  \
#   17   0

a = TreeNode(5)
b = TreeNode(8)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(45)
f = TreeNode(17)
g = TreeNode(0)

a.left = b
a.right = c
c.left = d
c.right = e
d.left = f
d.right = g

# a = TreeNode(-3)
# b = TreeNode(-1)

# a.left = b

s = Solution()
s.maxPathSum(a)