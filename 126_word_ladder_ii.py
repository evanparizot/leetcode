from typing import List
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or endWord not in wordList:
            return []
        
        wlength = len(beginWord)

        # Generate lookup dictionary
        lookup = defaultdict(list)
        for word in wordList:
            for i in range(wlength):
                key = word[:i] + '#' + word[i+1:]
                lookup[key].append(word)

        # Maintain visited set with mapping to parent instead
        visited = {beginWord:None}

        # Process current linkage and append to result
        q = [beginWord]
        result = []
        while q:
            word = q.pop(0)

            # Generate possible word permutations
            for i in range(wlength):
                key = word[:i] + '#' + word[i+1:]

                for related in lookup[key]:
                    if related == endWord:
                        # Need to generate path based on visited lookup
                        ans = [word, related]
                        parent = visited[word]
                        while parent:
                            ans.insert(0, parent)
                            parent = visited[parent]
                        
                        result.append(ans)

                    elif related not in visited:
                        visited[related] = word
                        q.append(related)

        min_length = min(len(x) for x in result)

        return [x for x in result if len(x) == min_length]

s = Solution()
print(s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
# print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))