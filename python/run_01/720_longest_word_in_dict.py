from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        used, res = set(), ""
        used.add("")
        for w in words:
            if w[:-1] in used:
                if len(w) > len(res):
                    res = w
                used.add(w)

        return res

s = Solution()
s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
s.longestWord(["w","wo","wor","worl", "world"])