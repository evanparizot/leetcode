
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:

        if not head:
            return None

        lookup = {}
        # Need to generate lookup for each node to node clone
        node = head
        while node:
            lookup[node] = Node(node.val)
            node = node.next

        # Need to iterate through original list and do lookups for next and random
        node = head
        while node:
            # Assign clone's next
            if node.next:
                lookup[node].next = lookup[node.next]

            # Assign clone's random
            if node.random:
                lookup[node].random = lookup[node.random]
            
            node = node.next

        return lookup[head]


