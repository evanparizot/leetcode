# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# LC # 25
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
