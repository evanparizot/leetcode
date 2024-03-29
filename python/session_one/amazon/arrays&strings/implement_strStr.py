# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # if not needle:
        #     return 0

        # left, right = 0, len(needle) -1
        # while right < len(haystack):
        #     sub = haystack[left:right+1]
        #     if sub == needle:
        #         return left
        #     left += 1
        #     right += 1
        
        # return -1

        L, n = len(needle), len(haystack)
        if L == 0:
            return 0
        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1
            
            if curr_len == L:
                return pn - L
            
            pn = pn - curr_len + 1
        return -1


s = Solution()
print(s.strStr("hello", "ll"))