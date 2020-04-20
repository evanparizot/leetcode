class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ""
        left = 0
        right = 0
        letters = list(t)
        while left <= len(s) - len(t) and right <= len(s): # If we have less letters left in string than target, no way can do this
            if all(c in s[left:right] for c in letters):
                # Current substring has all letters
                
                # Need to see if current substring has a short answer within it (maybe two 'a's)
                while left < right:
                    if all(c in s[left:right] for c in letters) and (answer == "" or len(answer) > len(s[left:right])):
                        answer = s[left:right]
                    left += 1
            else:
                right += 1
        return answer
s = Solution()
print(s.minWindow("aa","aa"))