from typing import List
from collections import deque
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Start with top left corner
        # If one, need to check right, down, diagonal
        # If valid, need to check next layer

        # def checkvalid(pair: tuple) -> bool:
        #     return ((0 <= pair[0] < len(matrix)) 
        #         and (0 <= pair[1] < len(matrix[pair[0]])) 
        #         and matrix[pair[0]][pair[1]] == "1")

        # max_area = 0

        # for row in range(len(matrix)):
        #     for col in range(len(matrix[row])):
        #         if matrix[row][col] == "1":
        #             # Do modified BFS
        #             # Queue up indices
        #             top_left = (row, col)
        #             q = deque([(row, col)])
        #             layer = 0
        #             while q:
        #                 tempq = deque()
        #                 valid_layer = True
        #                 # Need to process entire layer before increasing level
        #                 while q:
        #                     node_row, node_col = q.popleft()
                            
        #                     right = (node_row, node_col + 1)
        #                     below = (node_row + 1, node_col)
        #                     diagonal = (node_row + 1, node_col + 1)

        #                     # Add nodes accordingly
        #                     # Case to add right
        #                     if node_col == top_left[1] + layer:
        #                         if checkvalid(right):
        #                             tempq.append(right)
        #                         else:
        #                             valid_layer = False
        #                             break

        #                     # Case to add bottom
        #                     if node_row == top_left[0] + layer:
        #                         if checkvalid(below):
        #                             tempq.append(below)
        #                         else:
        #                             valid_layer = False
        #                             break

        #                     # Case to add diagonal
        #                     if (node_row == top_left[0] + layer 
        #                         and node_col == top_left[1] + layer):
        #                         if checkvalid(diagonal):
        #                             tempq.append(diagonal)
        #                         else:
        #                             valid_layer = False
        #                             break

        #                 # Check if inner while loop was exited prematurely
        #                 if valid_layer:
        #                     layer += 1
        #                     max_area = max(max_area, layer**2)
        #                     q = tempq
        #                 else:
        #                     break
        
        if matrix is None or len(matrix) < 1:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for col in range(cols+1)] for row in range(rows+1)]
        max_len = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min( dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_len = max(max_len, dp[i+1][j+1])
        return max_len**2


s = Solution()
test_case = [[1, 0, 1, 0, 0],
             [1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1], 
             [1, 0, 0, 1, 0]]

test_case2 = [[1, 0, 1, 0, 0],
             [1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1], 
             [1, 0, 1, 1, 1]]

test_case3 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
test_case4 = [["1", "1"]]
print(s.maximalSquare(test_case3))