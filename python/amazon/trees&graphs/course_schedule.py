from typing import List
class Solution():
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Solution One: Backtracking
        # ------------------------------------------
        # Step One: Build the Graph
        # Use an adjacency list (hashmap/dictionary)

        # Step Two: Enumerate each node (course) in the constructed graph, to check if we culd form a dependency cycle starting from the node

        # Step Three: We perform the cyclic check via backtracking, where we breadcrumb our path (mark nodes we've visited) to detect if
        # we come across a previously visited node (cycle). Remove the breadcrumbs for each iteration.





        # Solution Two: Postorder DFS
        # ------------------------------------------
        # The rationale is that given a node, if the subgraph formed by all descendant nodes from this node
        # has no cycle, then adding this node to the subgraph would not form a cycle either

        # Can use postorder traversal (visit child nodes before parent)

        # Step One: Build graph
        # Step Two: Enumerate each node in the constructed graph, to check if we could form a dependency cycle starting from the node
        # Step 3.1: We check if the current node has been checked before, otherwise we enumerate through it's child nodes via backtracking
        #           where we breadcrumb our path to detect if we come across a previously visited node.
        # Step 3.2: Once we visted all the child nodes, we mark the current node as checked




        # Solution Three: Topological Sort
        # -----------------------------------------
        # L = Empty list that will contain the sorted elements
        # S = Set of all nodes with no incoming edge

        # while S is non-empty do
        #     remove a node n from S
        #     add n to tail of L
        #     for each node m with an edge e from n to m do
        #         remove edge e from the graph
        #         if m has no other incoming edges then
        #             insert m into S

        # if graph has edges then
        #     return error   (graph has at least one cycle)
        # else 
        #     return L   (a topologically sorted order)