# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ans = -1
        
        dim = binaryMatrix.dimensions()
        py, px = 0, dim[1]-1 # Need to have first row and far right col
        
        # need to go to bottom left
        while py != dim[0]-1 or px >= 0:
            element = binaryMatrix.get(py, px)
            print('py: {}, px: {}, el: {}'.format(py,px,element))
            
            
            if element == 1:
                # Compare with ans
                if ans >= 0:
                    ans = min(ans, px)
                # To account for if this is the first 1 we've seen (ans will be -1)
                else:
                    ans = px
                
                # 'Advance' px left
                if px == 0:
                    break
                px -= 1
                
            elif element == 0:
                
                # If we see a zero and we're on the last row, we know we can't possibly find anything
                # further left
                if py == dim[0]-1:
                    break
                
                else:
                    py += 1
            
        return ans