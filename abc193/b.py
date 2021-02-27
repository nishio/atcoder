# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    INF = 9223372036854775807
    ret = INF
    for _i in range(N):
        A, P, X = map(int, input().split())
        if X > A:
            ret = min(P, ret)

    if ret == INF:
        print(-1)
    else:
        print(ret)


# tests
T1 = """
3
3 9 5
4 8 5
5 7 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
8
"""
T2 = """
3
5 9 5
6 8 5
7 7 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
-1
"""
T3 = """
10
158260522 877914575 602436426
24979445 861648772 623690081
433933447 476190629 262703497
211047202 971407775 628894325
731963982 822804784 450968417
430302156 982631932 161735902
880895728 923078537 707723857
189330739 910286918 802329211
404539679 303238506 317063340
492686568 773361868 125660016
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
861648772
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
