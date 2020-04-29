# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) 
# deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
# A common subsequence of two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP? Levenshtein Distance?
        # DP[i][j] = text1[0 ... i] & text2[0 ... j]

        # DP[i][j] = DP[i-1][j-1] + 1 if text1[i] == text2[j]
        #
        # otherwise
        # DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        # Approach two
        # Memoization Method
        # T = O(M*N), S = O(M*N)
        # Each subproblem takes O(1). With M*N subproblems we get O(M*N)

        # @lru_cache(maxsize = None)
        # def memo_solve(p1, p2):

        #     if p1 == len(text1) or p2 == len(text2):
        #         return 0
            
        #     # If the letters are the same, 'remove' both of them
        #     if text1[p1] == text2[p2]:
        #         return 1 + memo_solve(p1 + 1, p2 + 1)
        #     else:
        #         return max(memo_solve(p1, p2 + 1), memo_solve(p1+1, p2))
        # return memo_solve(0, 0)


        # Approach Three
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]



        # Approach Four
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text = text2, text1
        
        
        # The previous column starts with all 0's and like before is 1
        # more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            # Create a new array to represent the current column.
            current = [0] * (len(text1) + 1)
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one.
            previous = current
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]


s = Solution()
s.longestCommonSubsequence("abcde","ace") # -> 3
s.longestCommonSubsequence("abc", "def") # -> 0

