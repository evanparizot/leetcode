from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        crits = []
        adj_list = {x:[] for x in range(n)}

        for c in connections:
            adj_list[c[0]].append(c[1])
            adj_list[c[1]].append(c[0])
        
        for key, value in adj_list.items():
            if len(value) == 1:
                crits.append([key, value[0]])
        
        return crits


test_case = [[0,1],[1,2],[2,0],[1,3]]
s = Solution()
s.criticalConnections(4, test_case)