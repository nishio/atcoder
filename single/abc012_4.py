# included from snippets/main.py

from heapq import heappush, heappop


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, edges):
    INF = 9223372036854775807
    ret = INF

    for start in range(N):
        distances = [INF] * N
        distances[start] = 0
        queue = [(0, start)]
        while queue:
            d, frm = heappop(queue)
            if distances[frm] < d:
                # already know shorter path
                continue
            # if frm == goal:
            #     break
            for to in edges[frm]:
                new_cost = distances[frm] + edges[frm][to]

                if distances[to] > new_cost:
                    # found shorter path
                    distances[to] = new_cost
                    heappush(queue, (distances[to], to))
        ret = min(ret, max(distances))
    return ret


def main():
    # parse input
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
