from typing import List
from heapq import heappush, heappop
import re
class Solution():
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'\W+', ' ', paragraph.lower())
        words = paragraph.strip().split(' ')
        counts = {}
        # Could build a heap to store values (need word with max value)
        for w in words:
          if w.isalnum():
            if w in counts:
              counts[w] += 1
            else:
              counts[w] = 1
        
        heap = []
        for key in counts:
          heappush(heap, (-counts[key], key))

        while len(heap):
          _, w = heappop(heap)
          if w not in banned or not len(banned):
            return w
        
        

s = Solution()
s.mostCommonWord("a.", [])
# s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])