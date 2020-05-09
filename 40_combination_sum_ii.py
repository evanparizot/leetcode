class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], result)
        return result


    def dfs(self, nums, index, target, path, res):
        """
        Finds combinations that equal to input target, using unique

        Args:
            nums (List[int]): Numbers to choose from
            index (int):      
        """
        # Need to check if i == i-1: continue
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path + [nums[i]], res)