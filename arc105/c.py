# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, WS, VS, LS, VL):
    maxW = max(WS)
    maxV = max(VS)
    if maxW > maxV:
        return - 1
    # for all orders


def main():
    # parse input
    N, M = map(int, input().split())
    WS = list(map(int, input().split()))
    VS = []
    LS = []
    VL = []
    for _i in range(M):
        l, v = map(int, input().split())
        VL.append((v, l))
        LS.append(l)
        VS.append(v)

    print(solve(N, M, WS, VS, LS, VL))

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
