# Given an integer array "nums", find the contiguous subarray (containing at least one number) which has the largest sum and return it's sum.

from typing import List
import sys

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:

    # Time Complexity:
    # Since iterating over the arrays decreases with each step,
    # complexity is n(n + 1)/2

    # iterate over array and create max sum seen
    # update whenever encountering new max sum for given range
    # len_nums = len(nums)
    # maxx = nums[0]
    # for i in range(len_nums):
    #   result = 0
    #   for j in range(i, len_nums):
    #     result += nums[j]
    #     maxx = max(result, maxx)
    # return maxx


    # Time Complexity:
    # O(n log(n))
    #
    # Divide and conquer. Find the max sum coming out of left_half and right_half
    def max_cross_array(arr, l, m, r):
      summ = 0
      left_sum = - sys.maxsize
      right_sum = - sys.maxsize
      for i in range(m, l-1, -1):
        index = max(0,i)
        summ += arr[index]
        if summ > left_sum:
          left_sum = summ
      summ = 0
      for i in range(m + 1, r + 1):
        summ += arr[i]
        if summ > right_sum:
          right_sum = summ
      return left_sum + right_sum
    
    def max_sub_array(arr, l, r):
      if l == r:
        return arr[l]
      m = (r + l)//2
      return max(max_sub_array(arr,l,m), max_sub_array(arr, m+1,r), max_cross_array(arr, l,m,r))
    
    return max_sub_array(nums, 0, len(nums) - 1)



def main():
  s = Solution()
  s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) # [4,-1,2,1] (6)


if __name__ == "__main__":
  main()