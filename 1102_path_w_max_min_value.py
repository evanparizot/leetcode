from typing import List
import heapq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        
        # min_seen = A[0][0]

        # directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # visited = set()
        # coord = (0,0)

        # rows = len(A)
        # cols = len(A[0])

        # while coord != (rows-1, cols-1):
        #     # Get next coordinate
        #     next_spot = (float('-inf'), 0, 0)
        #     visited.add(coord)

        #     for d in directions:
        #         nrow, ncol = coord[0] + d[0], coord[1] + d[1]
        #         if 0 <= nrow < rows and 0 <= ncol < cols and (nrow, ncol) not in visited:
        #             val = A[nrow][ncol]
        #             if val > next_spot[0]:
        #                 next_spot = (val, nrow, ncol)
                
        #     min_seen = min(min_seen, next_spot[0])
        #     coord = (next_spot[1], next_spot[2])
        
        # return min_seen

        rows, cols = len(A), len(A[0])
        visited = [[0]*cols for _ in range(rows)]
        q = [(-A[0][0], 0, 0)]

        visited[0][0] = 1
        res = A[0][0]
        dirs = [(0,1), (0,-1), (1,0),(-1,0)]
        while q:
            v, row, col = heapq.heappop(q)
            if row == rows-1 and col == cols-1:
                return -v
            for drow, dcol in dirs:
                nrow = row + drow
                ncol = col + dcol
                if 0 <= nrow < rows and 0 <= ncol < cols and not visited[nrow][ncol]:
                    visited[nrow][ncol] = 1
                    heapq.heappush(q, (max(v, -A[nrow][ncol]), nrow, ncol))
        return -1


s = Solution()
test_case = [[5,4,5],[1,2,6],[7,4,6]]
test_case2 = [  [2,0,5,2,0],
                [2,4,4,4,3],
                [1,5,0,0,0],
                [5,4,4,3,1],
                [1,3,1,5,3]]
s.maximumMinimumPath(test_case)