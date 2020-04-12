# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    return (sum(set(nums))*2)-sum(nums)
