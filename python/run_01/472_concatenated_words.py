from functools import lru_cache
class Solution:
    # T = O(n*(l**2)(2**L))
    #       - n is number of words
    #       - l is the max length of a word

    def findAllConcatenatedWordsInADict(self, words):

        d = set(words) # S = O(n)
        
        @lru_cache(maxsize=None)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res