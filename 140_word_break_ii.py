from typing import List
class Solution:
    # T = O(N**3)
    # S = O(N**3)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [1] + [0] * len(s)
        wordDict = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
        result = []
        if dp[-1] == 0:
            return result

        def backtrack(index, s, path):
            if len(s) == 0:
                result.append(path[:-1])
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    backtrack(index + i, s[i:], path+s[:i]+ ' ')
        
        backtrack(0, s, '')
        return result

s = Solution()
s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])