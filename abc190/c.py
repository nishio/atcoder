# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, M = map(int, input().split())
    AB = []
    for _i in range(M):
        A, B = map(int, input().split())
        AB.append((A - 1, B - 1))
    K = int(input())
    CD = []
    for _i in range(K):
        C, D = map(int, input().split())
        CD.append((C - 1, D - 1))

    ret = 0
    for i in range(2 ** K):
        xs = [0] * N
        for j in range(K):
            cd = CD[j]
            if i & 1:
                xs[cd[0]] = 1
            else:
                xs[cd[1]] = 1
            i >>= 1
        r = 0
        for j in range(M):
            if xs[AB[j][0]] == xs[AB[j][1]] == 1:
                r += 1
        ret = max(ret, r)
    print(ret)


# tests
T1 = """
4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
4 4
1 2
1 3
2 4
3 4
4
3 4
1 2
2 4
2 4

"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
"""

T3 = """
6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6

"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
9
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
