# Best time to buy and sell stock II
# ---------------------------------------------

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie. buy one and sell one share of the stock 
# multiple times)

# eg.
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation:  Buy on day 2 (price = 1) and sell on day 3 (price = 5), 
#                 profit = 5-1 = 4
#               Then buy on day 4 (price = 3) and sell on day 5 (price = 6),
#                 profit = 6-3 = 3

# Stipulation:
# Cannot engage in multiple transactions at the same time (must sell the stock before you try again)

from typing import List
class Solution:
  def buySellOnlyTwice(self, prices: List[int]) -> int:
    max_prof, min_price_so_far = 0, 0
    first_buy_sell_profits = [0]*len(prices)

    for i, price in enumerate(prices):
      min_price_so_far = min(min_price_so_far, price)
      max_prof = max(max_prof, price - min_price_so_far)
      first_buy_sell_profits[i] = max_prof
    
    max_price_so_far = 0
    for i, price in reversed(list(enumerate(prices[1:], 1))):
      max_price_so_far = max(max_price_so_far, price)
      max_prof = max(max_prof, max_price_so_far - price + first_buy_sell_profits[i-1])
    return max_prof

  def buySellTwice(self, prices: List[float]) -> float:
    fb, fs, sb, ss = float('inf'), 0.0, float('inf'), 0.0
    for price in prices:
      fb = min(fb, price)     # Keep minimal
      fs = max(fs, price-fb)  # Maximum of one transaction
      sb = min(sb, price-fs)  # Total drop volume level
      ss = max(ss, price-sb)  # Maximum of sum of two transactions
    return ss

  def buySellAnyAmount(self, prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
      temp = prices[i]-prices[i-1]

      profit += max(temp, 0)
    return profit

    # return sum(max(prices[i]-prices[i-1], 0) for i in range(i, len(prices)))


  def buySellOnce(self, prices: List[int]) -> int:
    
    # Brute force
    # Outerloop invoked n-1 times
    # Since loop is getting smaller as a series, time complexity is
    # n(n-1)/2 or O(n^2)
    # -------------------------------------------------------------
    # max_diff = 0
    # for i in range(len(prices)):
    #   for j in range(i, len(prices)):
    #     max_diff = max(max_diff, prices[j]-prices[i])
    # return max_diff



    # Divide and conquer
    # https://keithschwarz.com/interesting/code/?dir=single-sell-profit
    # Can find the best result of the 1st and 2nd subarray and combine
    # Also need to consider if optimums appear in separate arrays
    #   so would need to find min in 1st array and max in 2nd array

    # 1. We should buy and sell purely in the left half of the array.
    # 2. We should buy and sell purely in the right half of the array.
    # 3. We should buy in the left half of the array and sell in the right half of
    #    the array.

    # T(n) = 2T(n/2) + O(n) = O(nlog(n))
    # -------------------------------------------------------------
    # if(len(prices) <= 1):
    #   return 0

    # left = prices[: len(prices)//2]
    # right = prices[len(prices)//2 :]
    # leftBest = self.buySellOnce(left)
    # rightBest = self.buySellOnce(right)

    # crossBest = max(right) - min(left)
    # return max(leftBest, rightBest, crossBest)



    # Divide and conquer (Improved)
    # 
    # -------------------------------------------------------------
    # if len(prices) == 0:
    #   return 0
    
    # def recursion(arr, lhs, rhs):
    #   if lhs == rhs:
    #     return (0, arr[lhs], arr[rhs])
      
    #   mid = lhs + (rhs - lhs) // 2 

    #   (leftProfit, leftMin, leftMax) = recursion(arr, lhs, mid)
    #   (rightProfit, rightMin, rightMax) = recursion(arr, mid + 1, rhs)

    #   maxProfit = max(leftProfit, rightProfit, rightMax - leftMin)
    #   return (maxProfit, min(leftMin, rightMin), max(leftMax, rightMax))
    
    # profit, _, _ = recursion(prices, 0, len(prices) - 1)
    # return profit

    # Dynamic Programming
    # T = O(n), M = O(1)
    # -------------------------------------------------------------
    if len(prices) == 0:
      return 0

    profit = 0
    cheapest = prices[0]
    for i in range(1, len(prices)):
      cheapest = min(cheapest, prices[i])
      profit = max(profit, prices[i] - cheapest)
    return profit


def main():
  s = Solution()
  s.buySellTwice([7,1,5,3,6,4])
  # s.buySellAnyAmount([7,1,5,3,6,4])  # 7
  # s.buySellAnyAmount([1,2,3,4,5])    # 4
  # s.buySellAnyAmount([7,6,4,3,1])    # 0

  # s.buySellOnce([40,50,30,60,20,70])
  # s.buySellOnce([310,315,275,295,260,270,290,230,255,250]) # 30

if __name__ == "__main__":
  main()