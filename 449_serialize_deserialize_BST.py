# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not values or values[-1] < lower or values[-1] > upper:
                return None
            val = values.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        values = [int(x) for x in data.split(' ') if x]
        return helper()

# Your Codec object will be instantiated and called as such:

a = TreeNode(10)
b = TreeNode(7)
c = TreeNode(15)

d = TreeNode(4)
e = TreeNode(12)
f = TreeNode(20)

a.left = b
a.right = c

b.left = d

c.left = e
c.right = f

codec = Codec()
# print(codec.serialize(a))
print(codec.deserialize("10,7,15,4,null,12,20"))
# codec.deserialize(codec.serialize(root))

