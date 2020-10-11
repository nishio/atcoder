# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, A, B):
    MOD = 10 ** 9 + 7  # 998_244_353
    if B > A:
        A, B = B, A
    return blute(N, A, B)
    allA = ((N - A + 1) ** 2) % MOD
    allB = ((N - B + 1) ** 2) % MOD
    AB = ((A + B - 1) ** 2) % MOD

    edge = (B - 1) * (A + B - 1)
    corner = (B - 1) ** 2
    bound = 4 * (edge - corner) * (N - A + 1)
    # s = 0
    # for i in range(1, B):
    #     pass
    # bound = (A + B - 1) * (N - A - B) * 4
    # debug(allA, allB, AB, edge, corner, msg=":allA, allB, AB, edge, corner")

    ret = (allA * allB - allA * AB + bound)
    debug(ret, msg=":ret")
    return ret % MOD


def diff(N, A, B):
    return blute(N, A, B) - solve(N, A, B)


def blute(N, A, B):
    ret = 0
    for ax in range(0, N - A + 1):
        for ay in range(0, N - A + 1):
            for bx in range(0, N - B + 1):
                for by in range(0, N - B + 1):
                    if ax <= bx < ax + A or ax < bx + B <= ax + A:
                        if ay <= by < ay + A or ay < by + B <= ay + A:
                            continue
                    ret += 1
    return ret


def main():
    # parse input
    N = int(input())
    for _i in range(N):
        N, A, B = map(int, input().split())
        print(solve(N, A, B))


# tests
T1 = """
9
3 1 1
3 2 1
3 2 2
4 2 2
4 3 2
4 3 3
5 2 2
5 3 2
5 3 3
"""


TEST_T1 = """
>>> as_input(T1)
>>> main()
72
20
0
32
0
0
156
44
0
"""

T2 = """
1
331895368 154715807 13941326
"""
_TEST_T2 = """
>>> as_input(T2)
>>> main()
result
"""

T3 = """
14
10 2 1
10 2 2
10 3 1
10 3 2
10 3 3
10 4 1
10 4 2
10 4 3
10 4 4
10 5 1
10 5 2
10 5 3
10 5 4
10 5 5
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
7776
5936
5824
4284
2940
4116
2880
1840
1032
2700
1760
1008
468
140
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
