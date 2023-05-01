from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        heap = [(-value, key) for key, value in a.items()]
        heapq.heapify(heap)
        answer = []
        for i in range(k):
            answer.append((heapq.heappop(heap))[1])
        return answer

        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)

s = Solution()
s.topKFrequent([2,3,1,2,1,1], 2)
s.topKFrequent([1,1,1,2,2,3], 2)