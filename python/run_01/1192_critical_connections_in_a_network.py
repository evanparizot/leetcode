from typing import List
from collections import defaultdict
class Solution:

    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/601695/Cleanest-and-Easiest-Understand-Python-Solution-99-Time-100-Mem
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        depths = [-1]*n
        results = []

        def dfs(prev_node, cur_node, cur_depth):
            depths[cur_node] = cur_depth
            min_depth = cur_depth
            for neighbor in graph[cur_node]:
                if neighbor == prev_node: continue

                # Find the temporary depth reached by a neighbor
                temp_depth = depths[neighbor]

                # If -1, means we never visited it. Assign it's depth to current depth + 1
                if temp_depth == -1:
                    temp_depth = dfs(cur_node, neighbor, cur_depth+1)
                
                # If the returned depth is deeper than the current depth, it's a CRITICAL CONNECTION
                # If not, then update the min_depth
                #
                # NOTE: We are comparing the 'returned depth from neighbor (temp_depth)' to the 'current depth reached by DFS' rather
                # than the 'min_depth' that is going to be returned. Because once the temp_depth is returned by a neighbor, it 
                # is the minimum depth of it
                if temp_depth > cur_depth:
                    results.append([cur_node, neighbor])
                else:
                    min_depth = min(min_depth, temp_depth)

            # Return the minimum depth reached by a node (temp_depth return above)
            depths[cur_node] = min_depth
            return min_depth
        
        dfs(None, 0, 0)
        return results


test_case = [[0,1],[1,2],[2,0],[1,3]]
s = Solution()
s.criticalConnections(4, test_case)