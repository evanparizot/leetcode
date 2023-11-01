class Solution:
    def numDecodings(self, s: str) -> int:
        # Need to find all permutations that are two digits long, <= 26
        
        l = len(s)
        dp = [1] + [0]*l

        for i in range(1, l + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                temp = int(s[i-2:i])
                dp[i] += dp[i-2]
            
        return dp[l]

s = Solution()
s.numDecodings("226")