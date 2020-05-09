from typing import List
class Solution:
    def isValidSudoku2(self, board):
        seen = sum( ([(c,i), (j, c), (i/3, j/3, c)] for i, row in enumerate(board) for j, c in enumerate(row) if c != '.'), [])
        return len(seen) == len(set(seen)) 


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {x:set() for x in range(9)}
        cols = {x:set() for x in range(9)}
        boxes = {x:set() for x in range(9)}

        mrows = len(board)
        ncols = len(board[0])

        # Iterate over each cell
        for r in range(mrows):
            for c in range(ncols):
                element = board[r][c]
                if element == '.': continue

                if element in rows[r]: return False
                else: rows[r].add(element)

                if element in cols[c]: return False
                else: cols[c].add(element)

                # Process boxes
                box_num = self.getBoxNumber(r,c)
                if element in boxes[box_num]: return False
                else: boxes[box_num].add(element)
        return True

    def getBoxNumber(self, row, col):
        if 0 <= row <= 2:
            if 0 <= col <= 2: return 0
            if 3 <= col <= 5: return 1
            if 6 <= col <= 8: return 2
        elif 3 <= row <= 5:
            if 0 <= col <= 2: return 3
            if 3 <= col <= 5: return 4
            if 6 <= col <= 8: return 5
        else:
            if 0 <= col <= 2: return 6
            if 3 <= col <= 5: return 7
            if 6 <= col <= 8: return 8




s = Solution()
test_case = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(test_case))