"""
Get Shortest Path (Dijkstra)

edges: dict<from:int, dict<to:int, cost:number>>
"""

from heapq import heappush, heappop


def shortest_path(
        start, goal, num_vertexes, edges,
        INF=9223372036854775807, UNREACHABLE=-1):
    distances = [INF] * num_vertexes
    prev = [None] * num_vertexes
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        d, frm = heappop(queue)
        if distances[frm] < d:
            # already know shorter path
            continue
        if frm == goal:
            path = [goal]
            p = goal
            while p != start:
                p = prev[p]
                path.append(p)
            path.reverse()
            return d, path
        for to in edges[frm]:
            new_cost = distances[frm] + edges[frm][to]
            if distances[to] > new_cost:
                # found shorter path
                distances[to] = new_cost
                prev[to] = frm
                heappush(queue, (distances[to], to))

    return UNREACHABLE

# --- end of library ---


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, S, T, edges):
    ret = shortest_path(S, T, N, edges)
    if ret == -1:
        print(-1)
        return
    dist, path = ret
    num_vertexes = len(path)
    print(dist, num_vertexes - 1)
    for i in range(num_vertexes - 1):
        print(path[i], path[i + 1])


def main():
    # verified https://judge.yosupo.jp/submission/28034
    N, M, S, T = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(dict)
    for _i in range(M):
        frm, to, cost = map(int, input().split())
        edges[frm][to] = cost
    solve(N, M, S, T, edges)


# tests
T1 = """
5 7 2 3
0 3 5
0 4 3
2 4 2
4 3 10
4 0 7
2 1 5
1 0 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
11 3
2 1
1 0
0 3
"""

T2 = """
2 1 0 1
1 0 10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
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

# end of snippets/main.py
