from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Generate adjacency list
        # Directed graph where [u,v] is u
        adj_list = defaultdict(list)

        for req in prerequisites:
            adj_list[req[0]].append(req[1])

        # Get in-degree zero nodes
        in_degree = [0] * numCourses

        # Traverse adj list to fill indegrees
        for i in adj_list:
            for j in adj_list[i]:
                in_degree[j] += 1
        
        # Create queue and enqueue all vertices with indegree zero
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # Count of visited vertices
        count = 0

        # Create vector to store result (Topological ordering of the vertices)
        top_order = []

        while queue:

            u = queue.pop(0)
            top_order.append(u)

            # Go through neighbor nodes and decrease indegree by 1
            for i in adj_list[u]:
                in_degree[i] -= 1

                # If indegree zero, then add to queue
                if in_degree[i] == 0:
                    queue.append(i)
            count += 1
        if count != numCourses:
            return False
        else:
            return True