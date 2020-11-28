# included from libs/iterate_all_subset.py
def iterate_all_subset_index(N):
    for i in range(2 ** N):
        ret = []
        for j in range(N):
            if i & 1:
                ret.append(j)
            i >>= 1
        yield ret


def sum_for_all_subset(XS):
    N = len(XS)
    ret = []
    for i in range(2 ** N):
        # init
        s = 0
        for j in range(N):
            if i & 1:
                # operation for selected vertexes
                s += XS[j]
            i >>= 1
        # do sth on result
        ret.append(s)
    return ret


def sum_for_all_subset_grey(XS):
    N = len(XS)
    ret = [0]
    # init
    s = 0
    prev = 0
    for i in range(1, 2 ** N):
        g = i ^ (i >> 1)  # to greycode
        x = mask = g ^ prev
        # ctz
        j = 0
        while x & 1 == 0:
            x >>= 1
            j += 1

        if g & mask:
            s += XS[j]
        else:
            s -= XS[j]
        # do sth on result
        ret.append(s)
        prev = g
    return ret


# end of libs/iterate_all_subset.py

# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, T, AS):
    from bisect import bisect_right
    S1 = []
    S1 = sum_for_all_subset_grey(AS[:N//2])
    S2 = sum_for_all_subset_grey(AS[N // 2:])
    S2.sort()
    ret = 0
    # debug(S1, S2, msg=":S1, S2")
    for x in S1:
        if x > T:
            continue
        i = bisect_right(S2, T - x)
        # debug(T-x, i, msg=":T-x, i")
        ret = max(ret, x + S2[i - 1])
    return ret


def main():
    N, T = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(N, T, AS))


# tests
T1 = """
5 17
2 3 5 7 11
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
17
"""

T2 = """
6 100
1 2 7 5 8 10
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
33
"""

T3 = """
6 100
101 102 103 104 105 106
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
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
