# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, M = map(int, input().split())
    s1 = 0
    for i in range(N):
        S = input().strip()
        s = S.count(b"1")
        if s % 2:
            s1 += 1
    print(s1 * (N - s1))

# tests
T1 = """
3 2
00
01
10
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""
T2 = """
7 5
10101
00001
00110
11110
00100
11111
10000
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
10
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