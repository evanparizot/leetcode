from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # stack = []
        # area = 0
        # for i in range(len(height)):
        #     offset = 0
        #     while stack and height[i] >= height[stack[-1]]:
        #         pre_i = stack.pop()
        #         area += (height[pre_i]-offset) * (i-pre_i - 1)
        #         offset = height[pre_i]
        #     if stack:
        #         area += (height[i]-offset) * (i - stack[-1]-1)
        #     stack.append(i)
        # return area

        water = []
        l = 0
        for h in height:
            l = max(l, h)
            water += [l] # over fill to left max height
        
        r = 0
        for i, h in reversed(list(enumerate(height))):
            r = max(r, h)
            water[i] = min(water[i], r) -h # drain to the right height
        
        return sum(water)

        # # Sliding Window
        # l, r = 0, len(height)-1
        # lmax = rmax = water = 0

        # while l < r:
        #     lmax = max(lmax, height[l])
        #     rmax = max(rmax, height[r])

        #     # The smaller height side is the maximum amount of rain water that can be trapped
        #     # (otherwise we would incorrectly add water that would spill over the smaller height side),
        #     # so add the number of units of water trapped from the smaller height side
        #     if lmax <= rmax:
        #         water += lmax - height[l]
        #         l += 1
        #     else:
        #         water += rmax - height[r]
        #         r -= 1
        # return water

test = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(test))