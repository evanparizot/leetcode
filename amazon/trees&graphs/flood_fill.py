# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]

# image = 
#[
#   [1, 1, 1],
#   [1, 1, 0],
#   [1, 0, 1]
# ]

# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.



from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # BFS?
        def changeColor(sr, sc, original):
            # Change color
            current = image[sr][sc]
            if current != original or current == newColor:
                return
            
            # Set new color
            image[sr][sc] = newColor

            # Recurse through neighbors
            if sr != 0: changeColor(sr - 1, sc, original)
            if sr != len(image)-1: changeColor(sr + 1, sc, original)
            if sc != 0: changeColor(sr, sc - 1, original)
            if sc != len(image[0])-1: changeColor(sr, sc + 1, original)

        original = image[sr][sc]
        if original == newColor:
            return image
        changeColor(sr, sc, original)

        return image

        # while len(q):
        #     # Get coordinate
        #     cr, cc = q.popleft()

        #     # Set in image

        #     # Add adjacent
        #     if cr != 0 and image[cr-1][cc] == source_val:
        #         q.append((cr-1, cc))
        #     if cr != len(image) and image[cr+1][cc] == source_val:
        #         q.append((cr+1, cc))
        #     if cc != 0 and image[cr][cc-1] == source_val:
        #         q.append((cr, cc-1))
        #     if cc != len(image[0]) and image[cr][cc+1] == source_val:
        #         q.append((cr, cc+1))

s = Solution()
print(s.floodFill([[0,0,0],[0,1,1]], sr = 1, sc = 1, newColor = 1))
# print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))