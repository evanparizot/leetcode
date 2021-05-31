from collections import deque
from typing import List
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q = deque([(r,c,'s')])
                    island_hash = ''
                    while q:
                        current_r, current_c, current_h = q.popleft()

                        grid[current_r][current_c] = 0

                        island_hash += current_h

                        for dy, dx, h in [(0,1,'l'),(0,-1,'r'),(1,0,'u'),(-1,0,'d')]:
                            next_r, next_c = current_r + dy, current_c + dx

                            if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == 1:
                                q.append((next_r, next_c, h))
                    
                    islands.add(island_hash)
        
        return len(islands)