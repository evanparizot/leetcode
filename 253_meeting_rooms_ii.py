from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # free = []
        
        # intervals.sort(key = lambda x: x[0])
        
        # heapq.heappush(free, intervals[0][1])
        
        # for i in intervals[1:]:
            
        #     if free[0] <= i[0]:
        #         heapq.heappop(free)
            
        #     heapq.heappush(free, i[1])
        # return len(free)

        intervals.sort(key = lambda x: x[0])
        heap = []
        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        return len(heap)


s = Solution()
s.minMeetingRooms([[0, 30],[5, 10],[15, 20]])