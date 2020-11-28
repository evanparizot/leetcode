# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        if not head.next: return head
        
        p = head
        length = 1
        
        # Get Length of linked list
        while p.next:
            p = p.next
            length += 1
        
        # Find displacement
        rotate = k%length
        
        if k == 0 or rotate == 0:
            return head
    
        fast = slow = head
        
        for i in range(rotate):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        
        slow.next = None
        fast.next = head
        head = temp
        
        return head

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

s = Solution()
s.rotateRight(a, 2)