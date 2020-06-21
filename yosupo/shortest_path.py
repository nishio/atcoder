from collections import defaultdict
from heapq import *
# fast input
import sys
input = sys.stdin.buffer.readline
INF = sys.maxsize

num_vertexes, num_edges, start, goal = map(int, input().split())

edges = defaultdict(dict)
distances = [INF] * num_vertexes
distances[start] = 0
shortest_path = defaultdict(list)
shortest_path[start] = []
for i in range(num_edges):
    a, b, c = map(int, input().split())
    edges[a][b] = c
    # edges[b][a] = c  # if bidirectional

queue = [(0, start)]
while queue:
    d, frm = heappop(queue)
    if distances[frm] < d:
        # already know shorter path
        continue
    if frm == goal:  # goal
        break
    for to in edges[frm]:
        if distances[to] > distances[frm] + edges[frm][to]:
            # found shorter path
            distances[to] = distances[frm] + edges[frm][to]
            heappush(queue, (distances[to], to))
            shortest_path[to] = (frm, to)

if distances[goal] == INF:
    # unreachable
    print(-1)
else:
    print(distances[goal])  # cost of shortest paath
    # to print shortest path as list of "v1 v2"
    path = []
    cur = goal
    while True:
        frm = shortest_path[cur]
        path.append((frm, cur))
        cur = frm
        if frm == start:
            break
    path.reverse()
    # print(len(path))  # edge count
    for p in path:
        print(*p)

    path = []
    cur = goal
    while True:
        frm, to = shortest_path[cur]
        path.append((frm, to))
        cur = frm
        if frm == start:
            break
    path.reverse()
    print(distances[goal], len(path))
    for frm, to in path:
        print(frm, to)
