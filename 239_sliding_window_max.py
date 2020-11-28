from collections import deque
from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # window = []
        # for i in range(k):
        #     window.append(nums[i])
        # l, r = 0, k
        # res = []
        # while r <= len(nums):
        #     # Get top
        #     heap = [-x for x in nums[l:r]]
        #     heapq.heapify(heap)
        #     res.append(-heap[0])

        #     l += 1
        #     r += 1
            
        # return res

        d = deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            if i >= k-1:
                out.append(nums[d[0]])
        return out

s = Solution()
s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)