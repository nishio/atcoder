"""
TSP: Travelling salesman problem / bit DP
"""


def tsp_return(num_vertex, distances):
    import sys
    INF = sys.maxsize

    SIZE = 2 ** num_vertex
    memo = [[INF] * num_vertex for _i in range(SIZE)]

    memo[0][0] = 0
    for subset in range(1, SIZE):
        for v in range(num_vertex):
            for u in range(num_vertex):
                mask = 1 << u
                if subset & mask:
                    memo[subset][v] = min(
                        memo[subset][v],
                        memo[subset ^ mask][u] + distances[u][v])
    return memo[-1][0]


def tsp_not_return(num_vertex, distances, from_start):
    # PAST3M
    SUBSETS = 2 ** num_vertex
    INF = 9223372036854775807
    memo = [[INF] * num_vertex for _s in range(SUBSETS)]

    for subset in range(1, SUBSETS):
        for v in range(num_vertex):  # new vertex
            mask = 1 << v
            if subset == 1 << v:
                # previous vertex is start
                memo[subset][v] = min(
                    memo[subset][v],
                    from_start[v])
            elif subset & mask:  # new subset includes v
                for u in range(num_vertex):
                    memo[subset][v] = min(
                        memo[subset][v],
                        memo[subset ^ mask][u] + distances[u][v])
    return min(memo[-1])

# --- end of library ---


def solve(N, XYZS):
    dist = []
    for i in range(N):
        a, b, c = XYZS[i]
        ds = []
        dist.append(ds)
        for j in range(N):
            p, q, r = XYZS[j]
            ds.append(abs(p - a) + abs(q - b) + max(0, r - c))

    return tsp_return(N, dist)


def main():
    # verified https://atcoder.jp/contests/abc180/tasks/abc180_e
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
