# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, K, dist):
    from itertools import permutations
    ret = 0
    for order in permutations(range(1, N)):
        d = 0
        prev = 0
        for x in order:
            d += dist[prev][x]
            prev = x
        # debug(order, d, msg=":order, d")
        d += dist[prev][0]
        if d == K:
            ret += 1
    return ret


def main():
    # parse input
    N, K = map(int, input().split())
    dist = []
    for _i in range(N):
        dist.append(list(map(int, input().split())))
    print(solve(N, K, dist))


# tests
T1 = """
4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
24
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
