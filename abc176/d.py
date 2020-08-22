#!/usr/bin/env python3
import sys
import numpy as np
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(H, W, Ch, Cw, Dh, Dw, data):
    data = list(data.reshape(-1))
    HEIGHT = H + 4
    WIDTH = W + 4
    N = HEIGHT * WIDTH
    visited = [0] * N
    distance = [0] * N
    jump = [0] * N
    from collections import deque

    start = (Ch + 1) * WIDTH + (Cw + 1)
    goal = (Dh + 1) * WIDTH + (Dw + 1)
    q = deque()
    q.append(start)

    currentDistance = 0
    while True:
        while q:
            p = q.pop()
            if visited[p]:
                continue
            if p == goal:
                return currentDistance
            distance[p] = currentDistance
            for dx in [-2, -1, 0, +1, +2]:
                for dy in [-WIDTH * 2, -WIDTH, 0, WIDTH, WIDTH * 2]:
                    jump[p + dx + dy] = currentDistance + 1
            visited[p] = 1
            for d in [-1, +1, -WIDTH, +WIDTH]:
                if data[p + d]:
                    q.append(p + d)

        # no continuous cell
        for i in range(HEIGHT * WIDTH):
            if not data[i]:
                continue
            if visited[i]:
                continue
            # not visited vacant cell
            if jump[i] > 0:
                q.append(i)
        currentDistance += 1
        if not q:
            return -1

    # print(distance)
    # print(visited.reshape((H+4, -1)))


def main():
    global data
    # parse input
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    data = np.array(list(read().strip()) + [0])
    data = np.equal(data, 46).reshape((H, W + 1))
    D = np.zeros((H + 4, W + 4), dtype=np.int8)
    D[2:2+H, 2:2+W+1] = data
    # print(data)
    # print(D)
    print(solve(H, W, Ch, Cw, Dh, Dw, D))


# tests
T1 = """
4 4
1 1
4 4
..#.
..#.
.#..
.#..
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
4 4
1 4
4 1
.##.
####
####
.##.
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""

T3 = """
4 4
2 2
3 3
....
....
....
....
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""

T4 = """
4 5
1 2
2 5
#.###
####.
#..##
#..##
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
2
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
