from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for col in range(cols + 1)] for row in range(rows + 1)]

        max_len = 0
        for i in range(rows):
            for j in range(cols):
                # Need to start setting numbers
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_len = max(max_len, dp[i+1][j+1])
        return max_len ** 2



        # rows = len(matrix)
        # cols = len(matrix[0])
        # dp = [0 for col in range(cols + 1)]
        # max_len, prev = 0, 0

        # for i in range(1, rows):
        #     for j in range(1, cols):
        #         temp = dp[j]
        #         if matrix[i-1][j-1] == "1":
        #             dp[j] = min( min(dp[j-1], prev), dp[j]) + 1
        #             max_len = max(max_len, dp[j])
        #         prev = temp
        # return max_len **2


testcase = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["0", "0", "0", "1", "0"]
]

s = Solution()
s.maximalSquare(testcase)