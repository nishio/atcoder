#!/usr/bin/env python3
# fast input
from heapq import heappop, heappush
import sys
input = sys.stdin.buffer.readline
INF = 10 ** 10
# INF = float("inf")

try:
    profile
except:
    def profile(f): return f

DEBUG = True
if DEBUG:
    def dp(*x):  # debugprint
        print(*x)
else:
    def dp(*x): pass


@profile
def main(H, W, K, x1, y1, x2, y2, mapdata):
    # H, W, K = map(int, input().split())
    # x1, y1, x2, y2 = map(int, input().split())
    # mapdata = sys.stdin.buffer.read().splitlines()
    # print(data)
    start = x1 * W + y1
    goal = x2 * W + y2

    #distances = {}
    distances = [(INF, 0)] * (H * W * 5)
    # defaultdict(lambda: (INF, 0))
    # distances[(start, 0)] = (0, 0)
    key = start * 5 + 4
    distances[key] = (0, 0)

    shortest_path = [0] * (H * W * 5)
    shortest_path[key] = 0

    queue = [((0, 0), key)]
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        (d, frac), pos_dir = heappop(queue)
        pos, direction = divmod(pos_dir, 5)
        x, y = divmod(pos, W)
        # dp("(frm, direction)", (frm, direction))
        # dp("distances[(frm, direction)]", distances[(frm, direction)])
        dist = distances[pos_dir]
        if dist < (d, frac):
            # already know shorter path
            continue
        if pos == goal:
            break

        # same direction
        # dp("direction", direction)
        if direction != 4:
            dx, dy = DIRS[direction]
            nx = x + dx
            ny = y + dy
            # dp("nx, ny", nx, ny)
            if mapdata[nx * W + ny]:
                if frac == 0:
                    newd = d + 1
                    newfrac = -K + 1
                else:
                    newd = d
                    newfrac = frac + 1
                newdist = (newd, newfrac)
                to = (nx * W + ny) * 5 + direction

                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir

        if direction < 2 or direction == 4:  # 0, 1, 4
            # facing X axis
            dir = 2
            nx = x
            ny = y + 1
            if mapdata[nx * W + ny]:
                newdist = (d + 1, -K + 1)

                to = (nx * W + ny) * 5 + dir
                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir

            dir = 3
            nx = x
            ny = y - 1
            if mapdata[nx * W + ny]:
                newdist = (d + 1, -K + 1)

                to = (nx * W + ny) * 5 + dir
                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir
        if direction > 1:  # 2, 3, 4
            # facing Y axis
            dir = 0
            nx = x + 1
            ny = y
            if mapdata[nx * W + ny]:
                newdist = (d + 1, -K + 1)

                to = (nx * W + ny) * 5 + dir
                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir

            dir = 1
            nx = x - 1
            ny = y
            if mapdata[nx * W + ny]:
                newdist = (d + 1, -K + 1)

                to = (nx * W + ny) * 5 + dir
                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir

        # dp("distances", distances)

    result = min(distances[goal * 5:goal * 5+4])
    if result[0] == INF:
        # unreachable
        return -1
    else:
        # cur = pos_dir
        # while cur != start * 5 and cur != 0:
        #     pos, direction = divmod(cur, 5)
        #     x, y = divmod(pos, W)
        #     print(cur, x, y, direction, distances[cur])
        #     cur = shortest_path[cur]
        return result[0]


# print(sys.argv)
if sys.argv[-1] == 'ONLINE_JUDGE':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8,i8,i8,i8,i8,i8,i8,b1[:])')(main)
    # b1[:],i8,i8,i8,i8,i8
    cc.compile()
    exit()
else:
    H, W, K = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    from my_module import main
    import numpy as np
    C = np.zeros((H + 2, W + 2), np.bool_)
    data = np.frombuffer(
        sys.stdin.buffer.read(),
        'S1')
    # print(data)
    data = data.reshape(H, -1)
    # print(data)
    data = data[:, : W] == b'.'
    # print(data)
    C[1: -1, 1: -1] = data
    C = C.ravel()
    H += 2
    W += 2

    print(main(H, W, K, x1, y1, x2, y2, C))
