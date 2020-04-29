class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i_total = 0
        n_total = 0
        
        for i, num in enumerate(nums):
            i_total += i
            n_total += num
        
        return (i_total + len(nums)) - n_total