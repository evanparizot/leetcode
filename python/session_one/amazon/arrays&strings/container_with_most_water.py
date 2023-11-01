# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms 
# a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        # Can have two pointers, slowly traveling inward
        # Stop once they are equal or left > right
        # Update max_seen based on min(left height, right height) * distance between the points

        max_seen = float('-inf')
        left, right = 0, len(height)-1

        while left < right:

            max_seen = max(max_seen, min(height[left], height[right])*(right-left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_seen

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))