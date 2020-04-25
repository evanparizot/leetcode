from typing import List
from collections import defaultdict
class Solution():
    def canJump(self, nums: List[int]) -> bool:
        # valid = set()
        # valid.add(0)
        # if not nums:
        #     return True

        # # Need to see if from index we can get to end of list
        # while valid:
        #     index = valid.pop()
            
        #     # If the index put in is last index or greater than
        #     if index >= len(nums)-1:
        #         return True

        #     # Need to add every index we can get to from here
        #     if nums[index] != 0:
        #         for i in range(1, nums[index]+1):
        #             valid.add(index + i)

        # return False

        # O(n^2)
        # memo = {k: -1 for k in range(len(nums))}
        # memo[len(nums)-1] = 1
        # for i in range(len(nums)-2, -1, -1):
        #     furthest = min(i + nums[i], len(nums)-1)
        #     for j in range(i+1, furthest+1):
        #         if memo[j] == 1:
        #             memo[i] = 1
        #             break

        # return memo[0] == 1

        # O(n)
        last = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0



s = Solution()
s.canJump([2,3,1,1,4])
s.canJump([3,2,1,0,4])