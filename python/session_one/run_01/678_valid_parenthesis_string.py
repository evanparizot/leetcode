class Solution:
    def checkValidString(self, s: str) -> bool:
        # low = hi = 0
        # for c in s:
        #     low += 1 if c == '(' else -1
        #     hi += 1 if c == ')' else -1
        #     if hi < 0:
        #         break
        #     low = max(low, 0)
        # return low == 0



        while s != s.replace("()", ""):
            s = s.replace("()", "")
        
        counter = 0
        for i in range(len(s)):
            if s[i] in ["(", "*"]:
                counter += 1
            else:
                if counter: counter -= 1
                else: return False
        
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] in [")", "*"]:
                counter += 1
            else:
                if counter: counter -= 1
                else: return False
        
        return True

s = Solution()
s.checkValidString("(**())")