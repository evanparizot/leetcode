class Solution():
    def threeSum(self, nums):
        # Two Pointer approach
        # ---------------------------------------------------
        def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
            lo, hi = i + 1, len(nums) -1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum < 0 or (lo > i+1 and nums[lo] == nums[lo-1]):
                    lo += 1
                elif sum > 0 or (hi < len(nums) -1 and nums[hi]==nums[hi+1]):
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i -1] != nums[i]:
                self.twoSumII(nums, i , res)
        return res




        # Hash set approach
        # ---------------------------------------------------
        res = []
        found, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        min_val = min((val1, val2, complement))
                        max_val = max((val1, val2, complement))
                        if (min_val, max_val) not in found:
                            found.add((min_val, max_val))
                            res.append([val1, val2, complement])
                    seen[val2] = i
        return res