from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Start in top left
        nrows = len(board)
        ncols = len(board[0])
        ship_count = 0

        # Could do a dfs in one direction, setting all the elements to '.'
        for i in range(nrows):
            for j in range(ncols):
                element = board[i][j]

                if element == '.':
                    continue
                
                # row element above is a '.' or col element to the left is a '.'
                if (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    ship_count += 1
        # Or just use reasoning about what constitutes the beginning of a battleship

        return ship_count