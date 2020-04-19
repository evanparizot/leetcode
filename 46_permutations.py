from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]
            other_permutations = self.permute(others)
            for permutation in other_permutations:
                result.append([nums[i]] + permutation)
        return result

s = Solution()
print(s.permute([1,2,3]))