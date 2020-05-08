from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)
        # One pass going forwards
        prod = 1
        for i, n in enumerate(nums):
            output[i] = output[i] * prod
            prod *= n

        prod = 1
        for i, n in reversed(list(enumerate(nums))):
            output[i] = output[i] * prod
            prod *= n
        
        return output

s = Solution()
s.productExceptSelf([1,2,3,4])