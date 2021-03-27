# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    INF = 9223372036854775807
    MAX = [-INF] * (N + 1)
    MIN = [INF] * (N + 1)
    for i in range(N):
        X, C = map(int, input().split())
        MAX[C] = max(MAX[C], X)
        MIN[C] = min(MIN[C], X)

    lx = 0
    rx = 0
    lt = 0
    rt = 0
    for c in range(N + 1):
        if MIN[c] == INF:
            continue
        l = MIN[c]
        r = MAX[c]
        lt2 = min(lt + abs(r - lx), rt + abs(r - rx)) + (r - l)
        rt2 = min(lt + abs(l - lx), rt + abs(l - rx)) + (r - l) 
        lx, rx, lt, rt = l, r, lt2, rt2
        # debug(lx, rx, lt, rt, msg=":")
    print(min(lt + abs(lx), rt + abs(rx)))

# tests
T1 = """
5
2 2
3 1
1 3
4 2
5 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
12
"""
T2 = """
9
5 5
-4 4
4 3
6 3
-5 5
-3 2
2 2
3 3
1 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
38
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