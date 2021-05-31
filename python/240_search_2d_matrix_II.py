class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        def search(left, up, right, down):
            if left > right or up > down:
                return False
            
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right -left)//2
            
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search(left, row, mid-1, down) or search(mid+1, up, right, row-1)
        
        return search(0, 0, len(matrix[0])-1, len(matrix)-1)

s = Solution()
s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
5)