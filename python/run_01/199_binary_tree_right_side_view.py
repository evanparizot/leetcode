class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from collections import deque
def rightSideView(root: TreeNode) -> List[int]:
    # level order traversal

    answer = []
    nodeq = [root]

    while nodeq:
        # Need to pop off level
        node_list = nodeq.pop(0)

        last = node_list[-1]

        answer.append(last.val)

        temp_list = []
        for node in node_list:
            # Add children to queue
            if node.left:
                temp_list.append(node.left)
            if node.right:
                temp_list.append(node.right)
        
        if temp_list:
            nodeq.append(temp_list)
    
    return answer


#    1            <--- [1]
#  /   \
# 2     3         <--- [1,3]
#  \     \
#   5     4       <--- [1,3,]

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
e = TreeNode(4)

a.left = b
a.right = c
b.right = d
c.right = e

print(rightSideView(a))