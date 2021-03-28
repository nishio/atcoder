# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    AS.sort()
    MOD = 998_244_353
    ret = 0
    x = 0
    for a in AS:
        ret = (ret + a * (a + x)) % MOD
        x = (x * 2 + a) % MOD

    print(ret)

# tests
T1 = """
3
2 4 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
63
"""
T2 = """
1
10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
100
"""
T3 = """
7
853983 14095 543053 143209 4324 524361 45154
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
206521341
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