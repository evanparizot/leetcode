from typing import List
class Solution():
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l<r:
            left, right = nums[l], nums[r]

            if left + right == t:
                return [l, r]

            if left + right > t:
                r -= 1
            else:
                l += 1


s = Solution()
print(s.twoSum([2,7,11,15], 9))