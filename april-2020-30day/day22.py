from typing import List
from collections import defaultdict
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k

class Solution():
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum, result = 0, 0
        lookup = defaultdict(int)
        lookup[0] = 1

        # while left < len(nums):
        # sum(i, j) = sum(0, j) - sum(0, i) where sum(i, j) represents the sum of all the elements from index i to j-1

        # What if a hashmap with keys as (i, j) = sum between those indicies
        for n in nums:
            csum += n
            if csum-k in lookup:
                result += lookup[csum-k]

            lookup[csum] += 1
        
        return result

s = Solution()
s.subarraySum([3,4,7,2,-3,1,4,2], 7)