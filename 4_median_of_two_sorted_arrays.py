from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge arrays?

        out = []
        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                out.append(nums1[n1])
                n1 += 1
            elif nums1[n1] > nums2[n2]:
                out.append(nums2[n2])
                n2 += 1
            elif nums1[n1] == nums2[n2]:
                out.append(nums1[n1])
                out.append(nums2[n2])
                n1 += 1
                n2 += 1
        
        while n1 < len(nums1):
            out.append(nums1[n1])
            n1 += 1
        while n2 < len(nums2):
            out.append(nums2[n2])
            n2 += 1
        
        # Check if odd
        if len(out) % 2 == 1:
            mid = len(out)//2
            return float(out[mid])
        # Check if even
        else:
            mid = len(out)//2
            ans = (out[mid] + out[mid-1])/2
            return ans

s = Solution()
s.findMedianSortedArrays([1,2],[3,4])