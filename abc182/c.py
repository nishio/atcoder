# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N):
    total = sum(N) % 3
    if total == 0:
        return 0

    if len(N) == 1:
        return -1

    from collections import Counter
    xs = Counter(x % 3 for x in N)
    if xs[total]:
        return 1

    if len(N) == 2:
        return -1

    if xs[1] > 1 or xs[2] > 1:
        return 2
    return -1


def main():
    # parse input
    N = [x - ord('0') for x in input().strip()]
    print(solve(N))


# tests
T1 = """
35
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
369
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
6227384
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1
"""

T4 = """
11
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
-1
"""

T5 = """
12
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
0
"""

T6 = """
3
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
-1
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
