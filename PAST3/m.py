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
# included from libs/coordinate_compression.py
"""
Coordinate compression (CoCo) / Zahyo Asshuku
"""


class CoordinateCompression:
    def __init__(self, values=None):
        if not values:
            values = []
        self.values = values[:]

    def add(self, x):
        self.values.append(x)

    def compress(self):
        self.values.sort()
        x2i = {}
        for i, x in enumerate(self.values):
            x2i[x] = i
        self.x2i = x2i
        self.i2x = self.values
        return self.x2i, self.i2x

# end of libs/coordinate_compression.py
# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, edges, S, K, TS):
    cc = CoordinateCompression(TS)
    v2i, _i2v = cc.compress()

    # dijkstra
    from collections import defaultdict
    distances = defaultdict(dict)
    ds = one_to_all(S, N, edges)
    from_start = {}
    for t in TS:
        from_start[v2i[t]] = ds[t]

    for t in TS:
        ds = one_to_all(t, N, edges)
        for t2 in TS:
            distances[v2i[t]][v2i[t2]] = ds[t2]

    # tsp
    num_vertex = K
    SUBSETS = 2 ** num_vertex
    INF = 9223372036854775807
    memo = [[INF] * num_vertex for _s in range(SUBSETS)]

    for subset in range(1, SUBSETS):
        for v in range(num_vertex):  # new vertex
            mask = 1 << v
            if subset == 1 << v:
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


def main():
    # parse input
    N, M = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(dict)
    for _i in range(M):
        frm, to = map(int, input().split())
        edges[frm-1][to-1] = 1  # -1 for 1-origin vertexes
        edges[to-1][frm-1] = 1  # if bidirectional

    S = int(input()) - 1
    K = int(input())
    TS = list(x - 1 for x in map(int, input().split()))
    print(solve(N, M, edges, S, K, TS))


# tests
T1 = """
3 2
1 2
2 3
2
2
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
5 5
1 2
1 3
1 4
1 5
2 3
1
3
2 3 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
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
