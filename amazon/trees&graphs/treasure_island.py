from typing import List
from collections import deque
class Solution():
    def treasureIsland(self, grid: List[List[str]]) -> int:
        def isValid(i, j, grid):
            return i >= 0 and i < len(grid) and j >=0 and j < len(grid[i]) and grid[i][j] != 'D'

        queue = deque((0,0))
        grid[0][0] = 'D'
        
        steps = 0
        while queue:
            tempq = deque()
            while queue:
                y, x = queue.popleft()

                if isValid(y, x, grid):
                    if grid[y][x] == 'X':
                        return steps
                    tempq.append((y+1, x))
                    tempq.append((y-1, x))
                    tempq.append((y, x+1))
                    tempq.append((y, x-1))
                    grid[y][x] = 'D'

            steps += 1
            queue = tempq
        
        return steps

