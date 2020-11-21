# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(S, P):
    n = P

    i = 1
    while i * i <= n:
        if n % i == 0:
            s = i + n // i
            if S == s:
                return "Yes"
        i += 1
    return "No"


def main():
    S, P = map(int, input().split())
    print(solve(S, P))


# tests
T1 = """
3 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
1000000000000 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""

T3 = """
6 9
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
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
