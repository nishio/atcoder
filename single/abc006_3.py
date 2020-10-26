# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# def solve(N, M):
#     q, r = divmod(M, N)
#     IMPOSSIBLE = (-1, -1, -1)
#     if q < 2:
#         return IMPOSSIBLE
#     if q > 4 or (q == 4 and r > 0):
#         return IMPOSSIBLE
#     if q == 2:
#         assert (N - r) * 2 + r * 3 == M
#         return (N - r, r, 0)
#     assert (N - r) * 3 + r * 4 == M
#     return (0, N - r, r)

def solve(N, M):
    IMPOSSIBLE = (-1, -1, -1)
    x = M - 2 * N
    if x < 0:
        return IMPOSSIBLE
    if x <= N:
        return (N - x, x, 0)
    x -= N
    if x <= N:
        return (0, N - x, x)
    return IMPOSSIBLE


def main():
    # parse input
    N, M = map(int, input().split())
    print(*solve(N, M))


# tests


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
