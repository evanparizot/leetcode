class ListNode(): 
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        current = ans
        carry = False

        while l1 or l2 or carry:
            summed = 0
            
            if l1:
                summed += l1.val
                l1 = l1.next
            if l2:
                summed += l2.val
                l2= l2.next
            if carry:
                summed += 1

            if summed >= 10:
                carry = True
                current.val = summed - 10
            else:
                carry = False
                current.val = summed
            
            # Need to advance answer
            if l1 or l2 or carry:
                current.next = ListNode(0)
                current = current.next

        return ans


a1 = ListNode(1)
a2 = ListNode(5)
a3 = ListNode(8)

a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(8)
b3 = ListNode(3)

b1.next = b2
b2.next = b3

s = Solution()
blah = s.addTwoNumbers(a1, b1)
print(blah)