#!/usr/bin/env python3
# fast input
from heapq import heappop, heappush
import sys
input = sys.stdin.buffer.readline
INF = 10 ** 10
# INF = float("inf")


def main(H, W, K, x1, y1, x2, y2, mapdata):
    start = x1 * W + y1
    goal = x2 * W + y2

    NUM_DIR = 4
    distances = [(INF, 0)] * (H * W * NUM_DIR)
    key = start * NUM_DIR
    distances[key] = (0, 0)
    distances[key + 2] = (0, 0)

    shortest_path = [0] * (H * W * NUM_DIR)
    shortest_path[key] = 0

    queue = [((0, 0), key), ((0, 0), key + 2)]
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        (d, frac), pos_dir = heappop(queue)
        pos, direction = divmod(pos_dir, NUM_DIR)
        x, y = divmod(pos, W)
        dist = distances[pos_dir]
        if dist < (d, frac):
            continue
        if pos == goal:
            break

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
            to = (nx * W + ny) * NUM_DIR + direction

            if distances[to] > newdist:
                # found shorter path
                distances[to] = newdist
                heappush(queue, (newdist, to))
                shortest_path[to] = pos_dir

        if direction < 2:
            # facing X axis
            dir = 2
            nx = x
            ny = y + 1
            if mapdata[nx * W + ny]:
                newdist = (d + 1, -K + 1)

                to = (nx * W + ny) * NUM_DIR + dir
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

                to = (nx * W + ny) * NUM_DIR + dir
                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir
        if direction > 1:
            # facing Y axis
            dir = 0
            nx = x + 1
            ny = y
            if mapdata[nx * W + ny]:
                newdist = (d + 1, -K + 1)

                to = (nx * W + ny) * NUM_DIR + dir
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

                to = (nx * W + ny) * NUM_DIR + dir
                if distances[to] > newdist:
                    # found shorter path
                    distances[to] = newdist
                    heappush(queue, (newdist, to))
                    shortest_path[to] = pos_dir

    result = min(distances[goal * NUM_DIR:goal * NUM_DIR + NUM_DIR])
    if result[0] == INF:
        # unreachable
        return -1
    else:
        return result[0]


# print(sys.argv)
if sys.argv[-1] == 'ONLINE_JUDGE':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i8(i8,i8,i8,i8,i8,i8,i8,b1[:])')(main)
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
