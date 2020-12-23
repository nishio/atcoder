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


def solve(HEIGHT, WIDTH, data):
    from collections import defaultdict
    edges = defaultdict(dict)
    W = WIDTH
    H = HEIGHT
    for level in range(10):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = x + y * WIDTH + level * WIDTH * HEIGHT
                v = data[y][x]
                if x < W - 1:
                    edges[pos + 1][pos] = 1
                if x > 0:
                    edges[pos - 1][pos] = 1
                if y < H - 1:
                    edges[pos + W][pos] = 1
                if y > 0:
                    edges[pos - W][pos] = 1
                if v == "S":
                    if level == 0:
                        start = pos
                elif v == "G":
                    if level == 9:
                        goal = pos
                else:
                    v = int(v)
                    if v == level:
                        edges[pos - W * H][pos] = 0

    return one_to_one(start, goal, 10 * W * H, edges)


def main():
    # parse input
    N, M = map(int, input().split())
    data = []
    for _i in range(N):
        data.append(input().strip().decode('ascii'))
    print(solve(N, M, data))


# tests
T1 = """
3 4
1S23
4567
89G1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
17
"""

T2 = """
1 11
S134258976G
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
20
"""

T3 = """
3 3
S12
4G7
593
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1
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
