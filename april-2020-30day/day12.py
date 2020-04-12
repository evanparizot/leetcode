# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Example:
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
from typing import List
from heapq import heapify, heappop, heappush
class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    # A max heap could work here
    # Remove two largest stones from heap
    
    # Calculate result
    # If stones are destroyed, then just get the next two
    # If stones are different, then get difference and return resulting stone to heap. Proceed to get next two stones.
    converted = [i*-1 for i in stones]
    heapify(converted)

    while len(converted) > 1:
      largest = heappop(converted) * -1
      second_largest = heappop(converted) * -1

      if largest > second_largest:
        largest = largest - second_largest
        heappush(converted, largest * -1)
      
    if len(converted) == 1:
      return heappop(converted) * -1
    else:
      return 0

s = Solution()
s.lastStoneWeight([1,2,3,4,5,6])
