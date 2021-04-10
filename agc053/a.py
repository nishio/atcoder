# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    S = input().strip().decode('ascii')
    AS = list(map(int, input().split()))

    XS = [0]
    for c in S:
        if c == "<":
            XS.append(XS[-1] + 1)
        else:
            XS.append(XS[-1] - 1)
    m = min(XS) + 1
    XS = [x + m for x in XS]

    ret = []
    while True:
        bs = [AS[i] - XS[i] for i in range(N + 1)]
        if any(x <= 0 for x in bs) or any(bs[i] == bs[i + 1] for i in range(N)):
            # not valid
            ret.append(AS)
            break
        ret.append(XS)
        AS = bs

    print(len(ret))
    for bs in ret:
        print(*bs)


# tests
T1 = """
3
<><
3 8 6 10
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
1 5 4 7
2 3 2 3
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
