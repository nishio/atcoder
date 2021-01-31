# included from libs/tsp.py
from heapq import heappush, heappop

"""
TSP: Travelling salesman problem / bit DP
"""


def tsp_return(num_vertex, distances):
    assert num_vertex < 20
    # ABC180E
    INF = 9223372036854775807
    SUBSETS = 2 ** num_vertex
    memo = [[INF] * num_vertex for _i in range(SUBSETS)]

    memo[0][0] = 0
    for subset in range(1, SUBSETS):
        for v in range(num_vertex):
            for u in range(num_vertex):
                mask = 1 << u
                if subset & mask:
                    memo[subset][v] = min(
                        memo[subset][v],
                        memo[subset ^ mask][u] + distances[u][v])
    return memo[-1][0]


def tsp_not_return(num_vertex, distances, from_start=None):
    """
    from_start: distance from a virtual start vertex (PAST3M)
    """
    assert num_vertex < 20
    if from_start == None:
        from_start = [0] * num_vertex

    INF = 9223372036854775807
    SUBSETS = 2 ** num_vertex
    memo = [[INF] * num_vertex for _i in range(SUBSETS)]

    for subset in range(1, SUBSETS):
        for v in range(num_vertex):  # new vertex
            mask = 1 << v
            if subset == mask:
                # previous vertex is start
                memo[subset][v] = min(
                    memo[subset][v],
                    from_start[v])
            elif subset & mask:  # new subset includes v
                for u in range(num_vertex):
                    memo[subset][v] = min(
                        memo[subset][v],
                        memo[subset ^ mask][u] + distances[u][v])
    return min(memo[-1])


# end of libs/tsp.py
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
    edges = defaultdict(list)
    for _i in range(M):
        frm, to = map(int, input().split())
        edges[frm - 1].append(to - 1)  # -1 for 1-origin vertexes
        edges[to - 1].append(frm - 1)  # if bidirectional

    K = int(input())
    CS = list(int(x) - 1 for x in input().split())

    INF = 9223372036854775807
    dist = []
    for c in CS:
        d = one_to_all_bfs(c, N, edges, INF)
        dd = [d[CS[i]] for i in range(K)]
        if INF in dd:
            print(-1)
            return
        dist.append(dd)

    ret = tsp_not_return(K, dist)
    print(ret + 1)


# tests
T1 = """
4 3
1 4
2 4
3 4
3
1 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
"""

T2 = """
4 3
1 4
2 4
1 2
3
1 2 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""

T3 = """
10 10
3 9
3 8
8 10
2 10
5 8
6 8
5 7
6 7
1 6
2 4
4
1 2 7 9
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
11
"""

T4 = """
3 3
3 2
2 1
1 3
3
1 2 3
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3
"""

T5 = """
4 3
1 4
2 4
3 4
4
1 2 3 4
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
5
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
