class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]

        # Need to generate DP matrix

        #dp[i][j] = dp[i-1][j] + dp[i][j-1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

s = Solution()
s.uniquePaths(m=7, n=3)