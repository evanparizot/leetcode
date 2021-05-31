from typing import List
class Solution:
    # T = O(n**2) to fill dp array
    # S = O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i: j+1] in wordDict:
                        dp[j+1] = True
        return dp[-1]

s = Solution()
s.wordBreak("leetcode", ["leet", "code"])