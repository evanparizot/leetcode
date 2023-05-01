class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (0,1), (-1,0), (0,-1),  (1,1), (-1,-1), (1,-1),(-1,1)]

        mrows = len(board)
        ncols = len(board[0])

        for r in range(mrows):
            for c in range(ncols):

                live_neighbors = 0

                # Check neighbors:
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc

                    if (0 <= new_row < mrows and 
                        0 <= new_col < ncols and
                        abs(board[new_row][new_col]) == 1):
                        live_neighbors += 1

                # Rule 1 and 3. Kill cell
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = -1

                # Rule 2
                if (live_neighbors == 2 or live_neighbors == 3) and abs(board[r][c]) == 1:
                    continue

                # Rule 4
                if live_neighbors == 3 and board[r][c] == 0:
                    board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0