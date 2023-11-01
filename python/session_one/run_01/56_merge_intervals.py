from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1:
            return intervals
        

        # Sort list, T = O(nlgn)
        sorted_list = sorted(intervals)
        i = 0
        while i < len(sorted_list)-1:
            first = sorted_list[i]
            second = sorted_list[i+1]
            # check if second start time in between first's start/finish
            if first[0] <= second[0] <= first[1]:
                # Need to take later of two finish times
                first[1] = max(first[1], second[1])
                del sorted_list[i+1]
            else:
                i += 1
        
        return sorted_list



s = Solution()
s.merge([[1,4],[4,5]])
s.merge([[1,3],[2,6],[15,18],[8,10]])