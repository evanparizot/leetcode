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


        infect = deque()
        fresh = 0

        row_m = len(grid)
        col_m = len(grid[0])

        # Get all infected
        for row in range(row_m):
            for col in range(col_m):
                if grid[row][col] == 2:
                    infect.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        # Maybe unecessary
        if len(infect) == 0:
            return -1

        infect.append((-1,-1))

        time = 0
        # need to start doing this directions list for iteration
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while infect:
            row, col = infect.popleft()
            # Need to add neighbors
            if row == -1:
                time += 1
                if infect:
                    infect.append((-1,-1))
            else:
                for d in directions:
                    n_row, n_col = row + d[0], col + d[1]


                    if row_m > n_row >=0 and col_m > n_col >= 0:
                        if grid[n_row][n_col] == 1:
                            # need to infect
                            grid[n_row][n_col] = 2
                            fresh -= 1
                            # need to add for next tainting
                            infect.append((n_row, n_col))
        return time - 1 if not fresh else -1

s = Solution()
s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])