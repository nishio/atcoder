# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    from collections import defaultdict
    edges = defaultdict(list)
    for _i in range(M):
        frm, to = map(int, input().split())
        edges[frm - 1].append(to - 1)  # -1 for 1-origin vertexes

    INF = 9223372036854775807
    minBuyCost = [INF] * N

    ret = -INF
    for i in range(N):
        ret = max(ret, AS[i] - minBuyCost[i])
        m = min(minBuyCost[i], AS[i])
        for j in edges[i]:
            minBuyCost[j] = min(minBuyCost[j], m)

    print(ret)


# tests
T1 = """
4 3
2 3 1 5
2 4
1 2
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
5 5
13 8 3 15 18
2 4
1 2
4 5
2 3
1 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
10
"""

T3 = """
3 1
1 100 1
2 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-99
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
