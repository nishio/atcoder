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

# --- end of library ---


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, edges):
    INF = 9223372036854775807
    ret = INF

    for start in range(N):
        distances = one_to_all(start, N, edges)
        debug(distances, msg=":distances")
        ret = min(ret, max(distances))
    return ret


def main():
    # verified https://atcoder.jp/contests/abc012/tasks/abc012_4
    N, M = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(dict)
    for _i in range(M):
        A, B, T = map(int, input().split())
        edges[A - 1][B - 1] = T
        edges[B - 1][A - 1] = T
    print(solve(N, M, edges))


# tests
T1 = """
3 2
1 2 10
2 3 10
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""

T2 = """
5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
26
"""

T3 = """
4 6
1 2 1
2 3 1
3 4 1
4 1 1
1 3 1
4 2 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1
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

# end of snippets/main.py
