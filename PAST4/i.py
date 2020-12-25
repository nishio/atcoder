# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, AS):
    import sys
    INF = sys.maxsize  # float("inf")

    from itertools import accumulate
    acc = list(accumulate(AS + AS)) + [0]

    def rangeSum(start, end):
        return acc[end - 1] - acc[start - 1]

    start = 0
    end = 1
    ret = INF
    total = rangeSum(0, N)
    while True:
        x = rangeSum(start, end)
        y = total - x
        d = x - y
        ret = min(abs(d), ret)
        if d < 0:
            if end == 2 * N - 1:
                break
            end += 1
        else:
            start += 1
    return ret


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


# tests
T1 = """
4
10 20 40 30
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
20
"""

T2 = """
20
13 76 46 15 50 98 93 77 31 43 84 90 6 24 14 37 73 29 43 9
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
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
