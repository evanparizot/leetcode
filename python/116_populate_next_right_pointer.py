
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # T = O(n)
    # S = O(n)
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        q = [root]
        
        while q:
            qlen = len(q)
            prev = None
            
            for _ in range(qlen):
                current = q.pop(0)
                if not prev:
                    prev = current
                else:
                    prev.next = current
                    prev = prev.next
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return root

    def connect2(self, root: Node) -> Node:
        if not root:
            return root
        
        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:

                # Same parent
                head.left.next = head.right

                # Same level, but different parents
                if head.next:
                    head.right.next = head.next.left

                head = head.next
            leftmost = leftmost.left
        return root