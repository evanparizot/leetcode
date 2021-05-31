"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None


        # T = O(n), S = O(n)
        # Generate node to clone lookup dictionary
        mappings = dict()
        current = head
        while current:
            mappings[current] = Node(current.val)
            current = current.next

        # Iterate back through original, doing mappings for the lookup clone
        current = head
        while current:
            # 1. Need to assign clone's next. Needs to be a clone (based on original node)
            if current.next is None:
                mappings[current].next = None
            else:
                mappings[current].next = mappings[current.next]

            # 2. Need to assign clone's random. Needs to be a clone (based on original node's orignal random clone)
            if current.random is not None:
                mappings[current].random = mappings[current.random]
            else:
                mappings[current].random = None
            
            current = current.next

        return mappings[head]




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

a.random = c
b.random = d
c.random = None
d.random = a

s = Solution()
s.copyRandomList(a)