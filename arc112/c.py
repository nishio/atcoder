# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def main():
    N = int(input())
    PS = [0] + [int(x) - 1 for x in input().split()]
    print(solve(N, PS))


def solve(N, PS):
    depth = [0] * N
    from collections import defaultdict
    children = defaultdict(list)
    for i in range(1, N):
        # debug(i, PS[i], depth[PS[i]], msg=":i, PS[i], depth[PS[i]]")
        depth[i] = depth[PS[i]] + 1
        children[PS[i]].append(i)
    # debug(depth, msg=":depth")
    # debug(children, msg=":children")

    cost = {}
    sign = {}
    for i in reversed(range(N)):
        if len(children[i]) == 0:
            cost[i] = 1
            sign[i] = -1
        elif len(children[i]) == 1:
            cost[i] = cost[children[i][0]] + 1
            sign[i] = sign[children[i][0]] * -1
        else:
            # choise
            cs = [(cost[x], sign[x]) for x in children[i]]
            rc = 0
            rs = 1
            for c, s in sorted(cs):
                if s == 1 and c < 0:
                    rc += rs * c
            for c, s in sorted(cs):
                if s == -1:
                    rc += rs * c
                    rs *= -1
            for c, s in sorted(cs):
                if s == 1 and c >= 0:
                    rc += rs * c
            cost[i] = rc + 1
            sign[i] = rs

    # debug(cost, sign, msg=":cost, sign")
    return (N + cost[0]) // 2


# tests
T1 = """
10
1 2 3 4 5 6 7 8 9
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""
T2 = """
5
1 2 3 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2
"""
T3 = """
10
1 1 3 1 3 6 7 6 6
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
5
"""

T4 = """
4
1 2 1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
2
"""

T5 = """
5
1 2 1 4
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
5
"""


def random_test():
    N = 5
    from random import seed, randint
    for s in range(10):
        seed(s)
        PS = [randint(0, i) for i in range(N - 1)]
        print(solve(N, PS))


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
