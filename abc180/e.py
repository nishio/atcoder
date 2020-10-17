# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, XYZS):
    global dist
    import sys
    sys.setrecursionlimit(10 ** 6)
    INF = sys.maxsize  # float("inf")

    dist = []
    for i in range(N):
        a, b, c = XYZS[i]
        ds = []
        dist.append(ds)
        for j in range(N):
            p, q, r = XYZS[j]
            ds.append(abs(p - a) + abs(q - b) + max(0, r - c))

    SIZE = 2 ** N
    memo = [INF] * SIZE
    memo[1] = 0
    last = [INF] * SIZE
    last[1] = 0

    GOAL = SIZE - 1

    memolast = [INF] * N
    for i in range(SIZE):
        # debug(i, msg=":i")
        if memo[i] == INF:
            continue
        for j in range(N):
            mask = 1 << j
            if i & mask:
                # already visited
                continue
            newpos = i | mask
            d = dist[last[i]][j]
            if newpos == GOAL:
                memolast[j] = min(memolast[j], memo[i] + d + dist[j][0])
            elif memo[newpos] > memo[i] + d:
                # debug(i, j, newpos, msg=":i,j")
                memo[newpos] = memo[i] + d
                last[newpos] = j
        # debug(memo, msg=":memo")
        # debug(last, msg=":last")

    # return memo[-1] + dist[last[-1]][0]
    debug(memolast, msg=":memolast")
    # return min(
    #     memolast[j]
    #     for j in range(N)
    # )
    return min(memolast)


def main():
    # parse input
    N = int(input())
    XYZS = []
    for _i in range(N):
        XYZS.append(list(map(int, input().split())))

    print(solve(N, XYZS))


# tests
T1 = """
2
0 0 0
1 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
9
"""

T2 = """
3
0 0 0
1 1 1
-1 -1 -1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
10
"""

T3 = """
17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
6519344
"""

T4 = """
4
0 0 0
0 0 1
0 1 1
0 1 0
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3
"""

T5 = """
4
0 0 0
0 0 1
0 1 0
0 1 1
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
3
"""

T6 = """
3
0 0 1
0 1 0
0 2 1
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
5
"""

T7 = """

"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
result
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
    as_input(T1)
    main()

# end of snippets/main.py
