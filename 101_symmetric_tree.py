from treenode import TreeNode
from collections import deque

def isSymmetric(root: TreeNode) -> bool:
  if not root:
    return True
  
  left = root.left
  right = root.right

  def check(t1, t2):
    if not t1 and not t2:
      return True
    if t1 and not t2:
      return False
    if not t1 and t2:
      return False
    if t1.val!=t2.val:
      return False
    return check(t1.left, t2.right) and check(t1.right, t2.left)
  
  return check(left, right)