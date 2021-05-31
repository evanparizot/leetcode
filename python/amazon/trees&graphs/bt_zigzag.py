# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels, level = [], 0
        from_right = False
        nodes = deque([root])
        while nodes:
            levels.append([])
            level_length = len(nodes)

            for _ in range(level_length):

                # If from right, treat like a queue
                if from_right:
                    node = nodes.popleft()
                    levels[level].append(node.val)
                    if node.right:
                        nodes.append(node.right)
                    if node.left:
                        nodes.append(node.left)

                # Otherwise treat like stack
                else:
                    node = nodes.pop()
                    levels[level].append(node.val)
                    if node.right:
                        nodes.insert(0, node.right)
                    if node.left:
                        nodes.insert(0, node.left)

            level += 1
            from_right = not from_right
        return levels

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# class Solution:
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         ret = []
#         level_list = deque()
#         if root is None:
#             return []
#         # start with the level 0 with a delimiter
#         node_queue = deque([root, None])
#         is_order_left = True

#         while len(node_queue) > 0:
#             curr_node = node_queue.popleft()

#             if curr_node:
#                 if is_order_left:
#                     level_list.append(curr_node.val)
#                 else:
#                     level_list.appendleft(curr_node.val)

#                 if curr_node.left:
#                     node_queue.append(curr_node.left)
#                 if curr_node.right:
#                     node_queue.append(curr_node.right)
#             else:
#                 # we finish one level
#                 ret.append(level_list)
#                 # add a delimiter to mark the level
#                 if len(node_queue) > 0:
#                     node_queue.append(None)

#                 # prepare for the next level
#                 level_list = deque()
#                 is_order_left = not is_order_left

#         return ret


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

s = Solution()
print(s.zigzagLevelOrder(a))