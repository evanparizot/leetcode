from functools import lru_cache
class Solution:
    # https://leetcode.com/problems/longest-common-subsequence/discuss/598508/Python-DP-solution-with-Explanation-%2B-Thinking-process-%2B-Diagram
    def longest(self, text1, text2):
        @lru_cache(maxsize = None)
        def memo_solver(ptr1, ptr2):
            # Base case
            # If either string is now empty, we can't match up anymore characters
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            # Recursive case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solver(ptr1+1, ptr2+1)

            # Recursive case 2
            else:
                return max(memo_solver(ptr1+1, ptr2), memo_solver(ptr1, ptr2+1))
        return memo_solver(0,0)


class Solution2():
    # T = O(mn) Solve m*n subproblems, with each solve costing O(1)
    # S = O(mn) 2D array size m*n
    def longest(self, text1, text2):
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):

                # If the same, then take from bottom right + 1
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]

class Solution3():
    def longest(self, text1, text2):

        # Make sure we use the shorter of the words
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        # Previous column starts with all zeros and is one larger than size of word
        previous = [0]*(len(text1) + 1)

        for col in reversed(range(len(text2))):

            current = [0]*(len(text1) + 1)

            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            previous = current
        
        return previous[0]

s = Solution()
# print(s.longest("abcde", "ace"))

s2 = Solution2()
s3 = Solution3()
print(s3.longest("abcde", "ace"))
"""
    a b c d e
   a          0
   c          0
   e          0
    0 0 0 0 0


"""