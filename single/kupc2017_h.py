# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M = map(int, input().split())
    VS = list(map(int, input().split()))
    HS = list(map(int, input().split()))

    points = [set() for i in range(N)]
    CS = []
    for _i in range(M):
        A, X, B, Y = tuple(map(int, input().split()))
        A -= 1
        B -= 1
        if HS[A] > 0 and X > 0:
            points[A].add(X - 1)
        if HS[B] < 0:
            points[B].add(Y)

        CS.append((A, X, B, Y))
    
    for i in range(N):
        if HS[i] > 0:
            points[i].add(VS[i])
        points 

    print(solve(SOLVE_PARAMS))

# tests


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