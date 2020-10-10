
#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, XS, YS):
    size = [0] * N
    x2y = [0] * N
    x2i = [0] * N
    for i in range(N):
        x2y[XS[i]] = YS[i]
        x2i[XS[i]] = i

    ymax = N - 1
    x = 0
    while x < N:
        start = x
        y0 = x2y[x]
        k = ymax - y0
        ymin = y0
        while k or ymax - ymin > x - start:
            x += 1
            y = x2y[x]
            if y0 < y:
                k -= 1
            ymin = min(ymin, y)
        end = x + 1
        s = end - start
        for x in range(start, end):
            size[x2i[x]] = s

        x += 1
        ymax = ymin - 1

    return size


def main():
    # parse input
    N = int(input())
    YS = []
    XS = []
    for _i in range(N):
        x, y = map(int, input().split())
        XS.append(x - 1)
        YS.append(y - 1)

    print(*solve(N, XS, YS), sep="\n")


# tests
T1 = """
4
1 4
2 3
3 1
4 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
1
2
2
"""

T2 = """
7
6 4
4 3
3 5
7 1
2 7
5 2
1 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
3
1
1
2
3
2
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


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
