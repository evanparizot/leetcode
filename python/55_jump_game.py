from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= last:
                last = i
        return last == 0

    def canJumpv2(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True

s = Solution()
s.canJumpv2([2,3,1,1,4])