# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # T = O(n ln(n))
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        mid = self.findmiddle(head)

        # Mid becomes root
        node = TreeNode(mid.val)

        # Base case when just one element in linked list
        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def findmiddle(self, head: ListNode):
        # The pointer used to disconnect the left half from the middle node
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # If slow as equal to head
        if prev:
            prev.next = None
        
        return slow

class Solution2():
    def maplltovalues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = self.maplltovalues(head)

        def convertListToBST(l, r):
            if l > r:
                return None
            
            mid = (l+r) // 2
            node = TreeNode(values[mid])

            # Base case when there is only one element left in the array
            if l == r:
                return None

            node.left = convertListToBST(l, mid -1)
            node.right = convertListToBST(mid + 1, r)
            return node
        
        return convertListToBST(0, len(values) -1)

class Solution3:
    # T = O(n)
    #       - Need to process each of the nodes in the linked list once
    # S = O(lgn)
    #       - Extra space is used by recursion stack. Due to being a height balanced BST, height is dictated by log(n)
    def sortedListToBST(self, head: ListNode):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)

    def convert(self, s, e):
        if s > e:
            return None
        mid = (s + e) // 2

        # First step of simulated inorder traversal. Recursively form left half
        l = self.convert(s, mid-1)

        # Once we've formed the left half, process the current node
        root = TreeNode(self.node.val)
        root.left = l

        # Maintain the invariance
        self.node = self.node.next

        # Recurse on the right hand side and form the BST out of them
        root.right = self.convert(mid + 1, e)
        return root