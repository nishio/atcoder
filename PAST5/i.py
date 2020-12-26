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
# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, K, HS, CS, ABS):
    from collections import defaultdict
    edges = defaultdict(dict)
    for i in range(M):
        frm, to = ABS[i]
        frm -= 1
        to -= 1
        if HS[frm] < HS[to]:
            to, frm = frm, to
        # reversed edge
        edges[to][frm] = 1

    goal = N
    for c in CS:
        edges[goal][c - 1] = 0

    distances = one_to_all(goal, N + 1, edges)
    INF = 9223372036854775807
    for i in range(N):
        d = distances[i]
        if d == INF:
            d = -1
        print(d)


def main():
    # parse input
    N, M, K = map(int, input().split())
    HS = list(map(int, input().split()))
    CS = list(map(int, input().split()))
    ABS = []
    for _i in range(M):
        ABS.append(tuple(map(int, input().split())))
    solve(N, M, K, HS, CS, ABS)


# tests
T1 = """
5 5 2
1 2 3 4 5
1 2
1 2
1 3
4 2
4 3
3 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
0
0
1
1
2
"""

T2 = """
5 6 2
6 5 9 15 3
4 2
1 5
2 5
2 4
1 3
4 3
2 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
0
2
0
-1
"""

T3 = """
5 4 2
3 10 5 8 2
3 5
3 2
3 1
4 5
2 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
1
0
1
0
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
