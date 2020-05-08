from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # the value 0 representing an empty cell;
        # the value 1 representing a fresh orange;
        # the value 2 representing a rotten orange.

        # Return the min number of minutes that must elapse until no cell has a fresh orange
        # If impossible, return -1

        # Need to know 

        # Need to do BFS search with a queue
        # Every time we empty the queue is a time period

        infected = deque()
        fresh = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    infected.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
                    
        if not infected:
            if not fresh:
                return 0
            else:
                return -1
        
        time = -1 
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while infected:
            for _ in range(len(infected)):
                row, col = infected.popleft()
                for d in directions:
                    nrow, ncol = row + d[0], col + d[1]
                    
                    if 0 <= nrow < rows and 0 <= ncol < cols:
                        if grid[nrow][ncol] == 1:
                            grid[nrow][ncol] = 2
                            fresh -= 1
                            infected.append((nrow, ncol))
            time += 1
        
        return time if not fresh else -1

s = Solution()
s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])