## Identifying Bridges

> Pseudocode
```python

id = 0
graph = defaultdict(list)
# n = size of graph

ids = [0]*n
low = [0]*n
visited = [False]*n

def findBridges():
    bridges = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges)
    return bridges

def dfs(at, parent, bridges):
    """Depth First Search to find bridges

    Arguments:
    at = current node
    parent = previous node
    bridges = list of found bridges

    """
    visited[at] = True
    id = id + 1
    low[at] = ids[at] = id

    # For each edge from node 'at' to node 'to'
    for to in graph[at]:
        if to == parent: continue
        if not visited[to]:
            dfs(to, at, bridges)

            # This happens on the callback
            low[at] = min(low[at], low[to])

            if ids[at] < low[to]:
                bridges.add(at)
                bridges.add(to)
        else:
            # Updates a node's min value if we see another node that we already visited with a lower value
            low[at] = min(low[at], ids[to)])

```