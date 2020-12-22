# included from snippets/main.py

from heapq import heappush, heappop


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# included from libs/dijkstra.py
"""
Get Distances of Shortest Path (Dijkstra)

edges: dict<from:int, dict<to:int, cost:number>>
"""


def one_to_one(
        start, goal, num_vertexes, edges,
        INF=9223372036854775807, UNREACHABLE=-1):
    distances = [INF] * num_vertexes
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        d, frm = heappop(queue)
        if distances[frm] < d:
            # already know shorter path
            continue
        if frm == goal:
            return d
        for to in edges[frm]:
            new_cost = distances[frm] + edges[frm][to]
            if distances[to] > new_cost:
                # found shorter path
                distances[to] = new_cost
                heappush(queue, (distances[to], to))

    return UNREACHABLE


def one_to_all(
        start, num_vertexes, edges,
        INF=9223372036854775807):

    distances = [INF] * num_vertexes
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        d, frm = heappop(queue)
        if distances[frm] < d:
            # already know shorter path
            continue
        for to in edges[frm]:
            new_cost = distances[frm] + edges[frm][to]

            if distances[to] > new_cost:
                # found shorter path
                distances[to] = new_cost
                heappush(queue, (distances[to], to))
    return distances


# end of libs/dijkstra.py

def solve(H, W, AS):
    from collections import defaultdict
    edges = defaultdict(dict)
    for x in range(W):
        for y in range(H):
            pos = y * W + x
            if x < W - 1:
                edges[pos + 1][pos] = AS[y][x]
            if x > 0:
                edges[pos - 1][pos] = AS[y][x]
            if y < H - 1:
                edges[pos + W][pos] = AS[y][x]
            if y > 0:
                edges[pos - W][pos] = AS[y][x]
    d1 = one_to_all(W - 1, H * W, edges)
    d2 = one_to_all(W * (H - 1), H * W, edges)
    d3 = one_to_all(W * H - 1, H * W, edges)
    INF = 9223372036854775807
    ret = INF
    for x in range(W):
        for y in range(H):
            pos = y * W + x
            v = d1[pos] + d2[pos] + d3[pos] - 2 * AS[y][x]
            if v < ret:
                ret = v

    return ret


def main():
    # parse input
    H, W = map(int, input().split())
    AS = []
    for _h in range(H):
        AS.append(list(map(int, input().split())))
    print(solve(H, W, AS))


# tests
T1 = """
5 6
9 9 9 9 1 0
9 9 9 9 1 9
9 9 9 1 1 1
9 1 1 1 9 1
0 1 9 9 9 0
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""

T2 = """
10 10
1 2 265 1544 0 1548 4334 9846 58 0
21 0 50 44 2 388 5 0 0 4
170 0 2 1 54 1379 50 3 41 0
310 0 1 0 2163 0 226 26 3 12
151 33 0 9 0 0 0 36 365 2286
0 3 12 3 9 317 645 100 21 4
52 1 569 0 144 0 6 202 25 0
8869 19 2058 1948 1252 1002 7 1750 0 5
0 3 8 29 2 4403 0 0 0 5
0 17 93 9367 159 6 1 216 0 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
246
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
