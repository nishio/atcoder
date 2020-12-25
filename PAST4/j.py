# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, X, S, ABC):
    INF = 1e+99
    from collections import defaultdict
    edges = defaultdict(dict)
    for A, B, C in ABC:
        edges[A - 1][B - 1] = C
        edges[B - 1][A - 1] = C

    warps = [[], [], []]
    for i in range(N):
        warps[S[i]].append(i)

    usedWarp = set()
    GOAL = N - 1
    START = 0

    from heapq import heappush, heappop, heapify
    queue = [(0, START)]
    mincost = [INF] * N
    mincost[START] = 0
    visited = [0] * N

    while True:
        cost, pos = heappop(queue)
        if pos == GOAL:
            return cost
        if visited[pos]:
            continue
        visited[pos] = 1
        ep = edges[pos]
        for next in ep:
            nc = cost + ep[next]
            if nc < mincost[next]:
                mincost[next] = nc
                heappush(queue, (nc, next))

        for typ in range(3):
            if typ == S[pos]:
                continue
            warp = S[pos] + typ - 1

            if (S[pos], typ) in usedWarp:
                continue

            c = X[warp]
            usedWarp.add((S[pos], typ))

            nc = cost + c
            for next in warps[typ]:
                if nc < mincost[next]:
                    mincost[next] = nc
                    heappush(queue, (nc, next))


def main():
    # parse input
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    S = [x - ord("A") for x in input().strip()]
    # debug(S, msg=":S")
    ABC = []
    for _i in range(M):
        ABC.append(list(map(int, input().split())))

    print(solve(N, M, X, S, ABC))


# tests
T1 = """
3 2
10 10 10
ABA
1 2 15
2 3 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
15
"""

T2 = """
3 2
10 1000000000 10
ABC
1 2 1000000000
2 3 1000000000
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
20
"""

T3 = """
5 6
5 10 15
ABCBC
5 4 4
3 5 2
1 3 7
3 4 1
4 2 1
2 3 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
8
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
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
