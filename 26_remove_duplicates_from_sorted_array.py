from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0
        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         del nums[i+1]
        #     else:
        #         i += 1
        # return len(nums)

        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])