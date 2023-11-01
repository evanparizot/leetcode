"""
Pseudocode for bridges:

id = 0
g = adjacency list with undirected edges
n = size of the graph

# In these arrays index i represents node i
ids = [0, 0, ..., 0] # length n
low = [0, 0, ..., 0] # length n
visited = [false, false, ..., false]

function findBridges():
  bridges = []
  # Finds all bridges in the graph across various connected components
  for (i = 0; i < n; i = i + 1):
    if(!visited[i]):
      dfs(i, -1, bridges)
  return bridges
  
#Perform DFS to find bridges. 
# at = current node
# parent = previous node
# The bridges list is always of even length and indexes (2*i, 2*i+1) form a bridge.
# For example, nodes at indexex (0,1) are a bridge, (2,3) is another, etc
function dfs(at, parent, bridges):
  visited[at] = true
  id = id + 1
  low[at] = ids[at] = id
  
  # For each edge from node 'at' to node 'to'
  for (to : g[at]):
    if to == parent: continue
    if (!visited[to]):
      dfs(to, at, bridges)
      
      # This min happens on the callback
      low[at] = min(low[at], low[to])
      if (ids[at] < low[to]):
        bridges.add(at)
        bridges.add(to)
    else:
      # Updates a node's min value if we see another node that we already visited with a lower value
      low[at] = min(low[at], ids[to])

"""

"""
Articulation Points

Simple observation about articulation points:
On a connected component with three or more vertices if an edge (u,v) is a bridge then either u or v is an articulation point

However, this condition alone is not sufficient to capture all articulation points. There exists cases where there is an articulation
point without a bridge

0     3
| \  / |
|   2  |
|  / \ |
 1     4

There are no bridges but node 2 is an articulation point since it's removal would cause the graph to split into two components.

ARTICULATION POINTS
On the callback, if id(e.from) == lowlink(e.to) then there was a cycle.
The indication of a cycle back to the original node implies an articulation point

The only time id(e.from) == lowlink(e.to) fails is when the starting node has 0 or 1 outgoing directed edges. This is because
either the node is a singleton (0 case) or the node is trapped in a cycle

    1
    | \
S-> 0  2
    | /
    3

Here the condition is met, but the starting node only has 1 outgoing edge. Therefore, the start node is NOT an articulation point.

id = 0
g = adjacency list
n = size of the graph
outEdgeCount = 0

ids = [0, 0, ..., 0] # length n
low = [0, 0, ..., 0] # length n
visited = [false, false, ..., false]
isArt = [false, false, ..., false]

function findArtPoints():
  for (i = 0; i < n; i = i + 1):
    if (!visited[i]):
      outEdgeCount = 0
      dfs(i, i, -1)
      isArt[i] = (outEdgeCount > 1)
  return isArt
  
function dfs(root, at, parent):
  if (parent == root): outEdgeCount += 1
  visited[at] = true
  id = id + 1
  low[at] = ids[at] = id
  
  # For each edge from node 'at' to node 'to'
  for (to : g[at]):
    if to == parent: continue
    if (!visited[to]):
      dfs(root, to, at)
      
      # This min happens on the callback
      low[at] = min(low[at], low[to])
      
      # Articulation point found via bridge
      if (ids[at] < low[to]):
        isArt[at] = true
      # Articulation point found via cycle
      if (ids[at] == low[to]):
        isArt[at] = true
    else:
      # Updates a node's min value if we see another node that we already visited with a lower value
      low[at] = min(low[at], ids[to])
"""
