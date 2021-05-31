# Given a non-empty, singly linked list with head node `head`, return a middle node of the linked list
# If there are two middle nodes, return the second middle node

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def middleNode(head: ListNode) -> ListNode:
  # Need to know length of the linked list
  # Could have two pointers, one iterating of every two iterations of the other
  # When 'faster' pointer reaches end, the 'slower' pointer should be about halfway through
  # length = 0
  # middle = current = head
  # while current.next:
  #   length += 1
  #   if length % 2 == 0:
  #     midde = middle.next
  #   current = current.next

  # if length % 2 == 1:
  #   middle = middle.next

  # return middle

  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow

