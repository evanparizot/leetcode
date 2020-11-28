class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def changeColor(sr, sc, original):
            if image[sr][sc] != original:
                return
            image[sr][sc] = newColor
            if sr != 0: changeColor(sr-1, sc, original)
            if sr != len(image) -1: changeColor(sr + 1, sc, original)
            if sc != 0: changeColor(sr, sc - 1, original)
            if sc != len(image[0])-1: changeColor(sr, sc + 1, original)
        
        if image[sr][sc] == newColor:
            return image
        changeColor(sr, sc, image[sr][sc])
        return image