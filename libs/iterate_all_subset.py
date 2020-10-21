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

# --- end of library ---


def pprint(xs):
    for x in xs:
        print(x)


TEST_T1 = """
>>> pprint(iterate_all_subset_index(4))
[]
[0]
[1]
[0, 1]
[2]
[0, 2]
[1, 2]
[0, 1, 2]
[3]
[0, 3]
[1, 3]
[0, 1, 3]
[2, 3]
[0, 2, 3]
[1, 2, 3]
[0, 1, 2, 3]
"""

TEST_T2 = """
>>> iterate_all_subset([1, 2, 3])
0
1
2
3
3
4
5
6
"""

TEST_T2 = """
>>> iterate_all_subset([1, 2, 3])
0
1
2
3
3
4
5
6
"""
TEST_T2 = """
>>> xs = list(sorted(sum_for_all_subset([1, 2, 3, 4])))
>>> ys = list(sorted(sum_for_all_subset_grey([1, 2, 3, 4])))
>>> xs == ys
True
"""


def ctz_naive(x, w=16):
    """
    counting zeros starting at the LSB until a 1-bit is encountered
    """
    if x == 0:
        return w
    t = 1
    r = 0
    while x & t == 0:
        t <<= 1
        r += 1
    return r


def ctz_ex0(x):
    """
    ctz except for zero
    """
    ret = 0
    while x & 1 == 0:
        x >>= 1
        ret += 1
    return ret


def to_graycode(x):
    return x ^ (x >> 1)


def sum_for_all_subset_grey_devel(XS):
    N = len(XS)
    ret = [0]
    # init
    s = 0
    for i in range(1, 2 ** N):
        g = to_graycode(i)
        mask = to_graycode(i) ^ to_graycode(i - 1)
        j = ctz_naive(mask)
        if g & mask:
            s += XS[j]
        else:
            s -= XS[j]
        # do sth on result
        ret.append(s)
    return ret


def main():
    for i in range(16):
        g = i ^ (i >> 1)
        print(f"{g:08b}")
        print(i & (-i), ctz_naive(g))


def _test():
    import doctest
    print("testing")
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        _test()
        sys.exit()
    main()
