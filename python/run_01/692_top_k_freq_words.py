from collections import Counter, defaultdict
import heapq
from typing import List
class Solution():
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]





print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))