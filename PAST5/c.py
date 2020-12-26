# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N):
    CS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = CS[N % 36]
    N //= 36
    while N > 0:
        ret = CS[N % 36] + ret
        N //= 36

    return ret


def main():
    # parse input
    N = int(input())
    print(solve(N))


# tests
T1 = """
123
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3F
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
