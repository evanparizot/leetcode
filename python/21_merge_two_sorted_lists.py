# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ans = ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                ans.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ans.next = ListNode(l2.val)
                l2 = l2.next
            
            ans = ans.next
            
        while l1:
            ans.next = ListNode(l1.val)
            l1 = l1.next
            ans = ans.next
        while l2:
            ans.next = ListNode(l2.val)
            l2 = l2.next
            ans = ans.next
        
        return head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

d.next = e
e.next = f

s = Solution()
s.mergeTwoLists(a, d)