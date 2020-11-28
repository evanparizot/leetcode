class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        pacific = [[]*len(matrix[0]) for _ in range(len(matrix))]
        atlantic = [[]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(0, len(matrix[0])):
            self.dfs(matrix, 0, i, float('-inf'), pacific)
            self.dfs(matrix, len(matrix)-1, i, float('-inf'), atlantic)
        
        for i in range(0, len(matrix)):
            self.dfs(matrix, i, 0, float('-inf'), pacific)
            self.dfs(matrix, i, len(matrix[0])-1, float('-inf'), atlantic)
        
        result = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if pacific[r][c] == 1 and atlantic[r][c] == 1:
                    result.append([r,c])
        return result

    def dfs(grid, r, c, prev, ocean):
        if r < 0 or c < 0 or r > len(grid) or c > len(grid[0]):
            return
        if grid[r][c] < prev:
            return
        if ocean[r][c] == 1:
            return

        # Process cell
        ocean[r][c] = 1

        self.dfs(grid, r-1, c, grid[r][c], ocean)
        self.dfs(grid, r+1, c, grid[r][c], ocean)
        self.dfs(grid, r, c-1, grid[r][c], ocean)
        self.dfs(grid, r, c+1, grid[r][c], ocean)
