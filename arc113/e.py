# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    print(solve(SOLVE_PARAMS))


def ex(N):
    import itertools
    for xs in itertools.product([0, 1], repeat=N):
        ret = []
        for i in range(N):
            for j in range(i + 1, N):
                if xs[i] == xs[j]:
                    ys = (
                        xs[:i] + tuple(reversed(xs[i + 1:j])) + xs[j+1:])
                    if ys > xs:
                        ret.append(ys)
        if ret:
            ret.sort()
            print(xs, ret[-1])
        else:
            print(xs)

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
