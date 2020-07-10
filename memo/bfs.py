from collections import deque

# convert bidirectional graph to tree
N = 100
edges = [[] for i in range(N)]
parent = [-1] * N
q = deque([0])
bfs_visited_order = []
while q:
    cur = q.popleft()
    bfs_visited_order.append(cur)
    for v in edges[cur]:
        if v != parent[cur]:
            parent[v] = cur
            edges[v].remove(cur)
            q.append(v)
