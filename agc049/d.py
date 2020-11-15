# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M):
    return blute(N, M)


# included from snippets/debug_indent.py
debug_indent = 0


def debug(*x, msg=" "):
    import sys
    global debug_indent
    x = list(x)
    indent = 0
    if msg.startswith("enter") or msg[0] == ">":
        indent = 1
    if msg.startswith("leave") or msg[0] == "<":
        debug_indent -= 1
    msg = "  " * debug_indent + msg
    print(msg, *x, file=sys.stderr)
    debug_indent += indent

# end of snippets/debug_indent.py


def debug_return_value(f):
    def g(x):
        debug(x, msg="<")
        return x

    def fg(*args, **kw):
        return g(f(*args, **kw))

    return fg


@debug_return_value
def blute(N, M, prev=None, slope=None):
    debug(N, M, prev, slope, msg=">N,M,prev,slope")
    if N == 0:
        if M != 0:
            return 0
        return 1

    if prev is None:
        return sum(
            blute(N - 1, M - x, x, None) for x in range(0, M + 1)
        )
    if slope is None:
        return sum(
            blute(N - 1, M - x, x, x - prev) for x in range(0, M + 1)
        )

    return sum(
        blute(N - 1, M - x, x, x - prev)
        for x in range(max(0, prev + slope), M + 1)
    )


def main():
    # parse input
    N, M = map(int, input().split())
    print(solve(N, M))


# tests
T1 = """
3 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
result
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
