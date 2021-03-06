# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    AS = []
    BS = []
    for _n in range(N):
        A, B = map(int, input().split())
        AS.append(A)
        BS.append(B)
    ret = INF = 9223372036854775807
    for i in range(N):
        for j in range(N):
            A = AS[i]
            B = BS[j]
            if i == j:
                v = A + B
            else:
                v = max(A, B)
            ret = min(ret, v)
    print(ret)

# tests
T1 = """
3
8 5
4 4
7 9
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
"""
T2 = """
3
11 7
3 2
6 7
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
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