# included from libs/dijkstra.py
"""
Get Distances of Shortest Path (Dijkstra)

edges: dict<from:int, dict<to:int, cost:number>>
"""


from heapq import heappush, heappop


def one_to_one(
        start, goal, num_vertexes, edges,
        INF=9223372036854775807, UNREACHABLE=-1):
    distances = [INF] * num_vertexes
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        # debug(queue, distances, msg=":queue, distances")
        d, frm = heappop(queue)
        if distances[frm] < d:
            # already know shorter path
            continue
        if frm == goal:
            return d
        for to, T, K in edges[frm]:
            # distance depents on currentTime
            currentTime = distances[frm]
            # debug(frm, to, currentTime, currentTime %
            #       K, T, msg=":frm, to, currentTime, currentTime % K, T")
            dist = (-currentTime % K) + T
            new_cost = currentTime + dist
            if distances[to] > new_cost:
                # found shorter path
                distances[to] = new_cost
                heappush(queue, (distances[to], to))

    return UNREACHABLE


# end of libs/dijkstra.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M, X, Y = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(list)
    for _m in range(M):
        A, B, T, K = map(int, input().split())
        edges[A - 1].append((B - 1, T, K))
        edges[B - 1].append((A - 1, T, K))

    INF = 9223372036854775807
    r = one_to_one(X - 1, Y - 1, N, edges, INF)
    if r == INF:
        r = -1
    print(r)


# tests
T1 = """
3 2 1 3
1 2 2 3
2 3 3 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
7
"""
T2 = """
3 2 3 1
1 2 2 3
2 3 3 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""
T3 = """
3 0 3 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
"""
T4 = """
9 14 6 7
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3
2 3 8 4
6 2 6 4
3 8 3 2
7 9 5 2
8 4 1 9
7 1 6 9
3 9 9 3
7 5 1 5
8 2 9 7
4 9 4 4
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
26
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
