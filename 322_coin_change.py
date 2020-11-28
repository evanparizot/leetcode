from typing import List
class Solution():
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        # dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                curr = dp[x]
                prev = dp[x-coin] + 1
                # elem = min(dp[x], dp[x-coin] + 1)
                # dp[x] = min(dp[x], dp[x-coin] + 1)
                dp[x] = min(curr, prev)
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
print(s.coinChange([5,2,1], 11))