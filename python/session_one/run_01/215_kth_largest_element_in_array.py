import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = [x * -1 for x in nums]
        heapq.heapify(l)

        if k > 1:
            for i in range(k-1):
                heapq.heappop(l)

        return (heapq.heappop(l))*-1

test_case = [3,2,3,1,2,4,5,5,6]
Solution().findKthLargest(test_case, 4)