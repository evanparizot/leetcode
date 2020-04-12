
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# Give a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the 
# longest path between any two nodes in a tree. This path may or may not pass through the root

# Ex:
#     1
#    / \
#   2   3
#  / \     
# 4   5    

# Return 3 (length of the path [4,2,1,3] or [5,2,1,3])

def diameterOfBinaryTree(root: TreeNode) -> int:
  # Probably need to do some sort of tree traversal
  # In order    L -> Root -> R
  # Pre order   Root -> L -> R
  # Post order  L -> R -> Root

  def traverse(node: TreeNode) -> tuple:
    value = 0
    max_seen = 0

    if node:
      left = traverse(node.left)
      right = traverse(node.right)

      max_seen = max(left[0] + right[0], left[1], right[1])
      value = max(left[0], right[0]) + 1
    return (value, max_seen)

  return traverse(root)[1]



a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')

# a.left = b
# a.right = c

# b.left = d
# b.right = e

a.left = b
b.left = c
b.right = d

print(diameterOfBinaryTree(a))