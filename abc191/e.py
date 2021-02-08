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


def one_to_all_bfs(start, num_vertexes, edges, INF=9223372036854775807):
    """
    when all cost is 1, BFS is faster (ABC170E)
    """
    distances = [INF] * num_vertexes
    distances[start] = 0
    to_visit = [start]
    while to_visit:
        next_visit = []
        for frm in to_visit:
            for to in edges[frm]:
                new_cost = distances[frm] + 1
                if new_cost < distances[to]:
                    distances[to] = new_cost
                    next_visit.append(to)
        to_visit = next_visit
    return distances

# end of libs/dijkstra.py


# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M = map(int, input().split())
    from collections import defaultdict
    INF = 9223372036854775807
    edges = defaultdict(lambda: defaultdict(lambda: INF))
    for _i in range(M):
        frm, to, cost = map(int, input().split())
        # -1 for 1-origin vertexes
        edges[frm-1][to-1] = min(edges[frm-1][to-1], cost)

    dist = []
    for start in range(N):
        dist.append(one_to_all(start, N, edges, INF=INF))

    for i in range(N):
        x = INF
        for j in range(N):
            if j == i:
                x = min(x, edges[i][i])
            else:
                x = min(x, dist[i][j] + dist[j][i])
        if x == INF:
            print(-1)
        else:
            print(x)


# tests
T1 = """
4 4
1 2 5
2 3 10
3 1 15
4 3 20
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
30
30
30
-1
"""

T2 = """
4 6
1 2 5
1 3 10
2 4 5
3 4 10
4 1 10
1 1 10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
10
20
30
20
"""

T3 = """
4 7
1 2 10
2 3 30
1 4 15
3 4 25
3 4 20
4 3 20
4 3 30
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
-1
40
40
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
