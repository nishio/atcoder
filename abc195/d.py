# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N,M,Q = map(int, input().split())
    WS = []
    VS = []
    for _n in range(N):
        W,V = map(int, input().split())
        WS.append(W)
        VS.append(V)
    XS = list(map(int, input().split()))
    WS.append(0) # sentinel
    VS.append(0)

    for _q in range(Q):
        L,R = map(int, input().split())
        box = XS[:L - 1] + XS[R:]
        box.sort()
        values = VS[:]
        ret = 0
        for size in box:
            maxv = 0
            maxi = -1
            for i in range(N):
                if WS[i] > size:
                    continue
                if values[i] > maxv:
                    maxv = values[i]
                    maxi = i
            values[maxi] = 0
            ret += maxv
        print(ret)

# tests
T1 = """
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
20
0
9
"""
T2 = """
3 4 3
2 10
3 10
4 10
1 2 3 4
4 4
3 4
2 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
20
10
0
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