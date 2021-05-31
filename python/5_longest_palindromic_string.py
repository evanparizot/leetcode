class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)



        # for i in range(len(s)):
        #     # Odd case
        #     temp = self.helper(s, i, i)
        #     if len(temp) > len(res):
        #         res = temp
            
        #     # Even case
        #     temp = self.helper(s, i, i+1)
        #     if len(temp) > len(res):
        #         res = temp
        return res
        
    # Get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]