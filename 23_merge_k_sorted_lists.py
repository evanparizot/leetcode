# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        ans = ListNode()
        head = ans
        
        for l in lists:
            if l:
                q.put((l.val, l))


        while q.not_empty():
            val, node = q.get()
            ans.next = ListNode(val)
            ans = ans.next
            node = node.next

            if node:
                q.put((node.val, node))

        return head.next

a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)


print(Solution().mergeKLists([a, b, c]))