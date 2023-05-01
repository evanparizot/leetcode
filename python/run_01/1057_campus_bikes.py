#  On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

# Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with 
# the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs 
# with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, 
# we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

# The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

# Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

# Example One
# -----------------------------
# Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# Output: [1,0]
# Explanation: 
# Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

# Example Two
# -----------------------------
# Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
# Output: [0,2,1]
# Explanation: 
# Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, 
# thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].

from typing import List
from collections import defaultdict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def manhattan(bike: list, worker: list) -> int:
            return abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])

        ans = [-1]*len(workers)
        distances = defaultdict(list)
        used = set()

        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[manhattan(bikes[j], workers[i])].append([i,j])
        
        for k in sorted(distances.keys()):
            for i in range(len(distances[k])):
                if ans[distances[k][i][0]] == -1 and distances[k][i][1] not in used:
                    ans[distances[k][i][0]] = distances[k][i][1]
                    used.add(distances[k][i][1])
        
        return ans

s = Solution()
s.assignBikes([[0,0],[2,1]], [[1,2],[3,3]])