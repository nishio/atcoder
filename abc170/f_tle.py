from collections import defaultdict
from heapq import *

# fast input
import sys
input = sys.stdin.buffer.readline
INF = 10 ** 10
# INF = float("inf")

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
map = sys.stdin.buffer.read().splitlines()
# print(data)
start = (x1, y1)
goal = (x2, y2)

distances = defaultdict(lambda: INF)
distances[start] = 0
shortest_path = {}
shortest_path[start] = None

maxdist = max(H, W)

leaf = ord("@")


def neighbor(frm):
    "return (to, cost)"
    x, y = frm
    # print("frm", frm)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x
        ny = y
        for dist in range(1, maxdist):
            nx += dx
            ny += dy
            if nx < 1 or H < nx or ny < 1 or W < ny:
                # print("out of bounds")
                break
            # print(nx, ny, data[nx - 1][ny - 1])
            if map[nx - 1][ny - 1] == leaf:
                # print("hit leaf")
                break
            cost = (dist - 1) // K + 1
            yield ((nx, ny), cost)


queue = [(0, start)]
while queue:
    d, frm = heappop(queue)
    # print("from", frm)
    if distances[frm] < d:
        # already know shorter path
        continue
    if frm == goal:  # goal
        break
    for to, cost in neighbor(frm):
        if distances[to] > distances[frm] + cost:
            # found shorter path
            distances[to] = distances[frm] + cost
            heappush(queue, (distances[to], to))
            shortest_path[to] = frm
    # print(distances)

if distances[goal] == INF:
    # unreachable
    print(-1)
else:
    path = []
    cur = goal
    print(distances[goal])

    # while True:
    #     frm = shortest_path[cur]
    #     path.append(frm)
    #     cur = frm
    #     if frm == start:
    #         break
    # path.reverse()
    # print(len(path))  # edge count
    # for (frm, to) in path:
    #     print(frm, to)
