class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return # backtracking
        for i in range(1, len(s) + 1):
            if self.ispalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    
    def ispalindrome(self, s):
        return s == s[::-1]