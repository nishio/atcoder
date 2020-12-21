# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# included from libs/fenwick_tree.py
"""
Fenwick Tree / Binary Indexed Tree (BIT)
"""


def init(n, value=0):
    global N, bit
    N = n
    bit = [value] * (N + 1)  # 1-origin


def bit_add(pos, val):  # point add / range sum
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] += val
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_set(pos, val):  # point set / range max
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] = max(bit[x], val)
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_point_action(pos, action_force, action):  # not tested
    assert pos > 0
    x = pos
    while x <= N:
        bit[x] = action_force(bit[x], action)
        x += x & -x  # (x & -x) = rightmost 1 = block width


def bit_max(pos):
    assert pos > 0
    ret = 0
    x = pos
    while x > 0:
        ret = max(ret, bit[x])
        x -= x & -x
    return ret


def bit_sum(pos):
    """
    sum includes x[pos]
    """
    ret = 0
    x = pos
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret


def bit_range_reduce(pos, value_binop, value_unity):  # not tested
    ret = value_unity
    x = pos
    while x > 0:
        ret = value_binop(ret, bit[x])
        x -= x & -x
    return ret


def bit_bisect(lower):
    "find a s.t. v1 + v2 + ... + va >= lower"
    x = 0
    k = 1 << (N.bit_length() - 1)  # largest 2^m <= N
    while k > 0:
        if (x + k <= N and bit[x + k] < lower):
            lower -= bit[x + k]
            x += k
        k //= 2
    return x + 1


# end of libs/fenwick_tree.py

def solve(H, W, M, PS):
    from operator import add
    ret = H * W - M

    init(200000 + 10)

    from collections import defaultdict
    P2 = defaultdict(list)
    for i in range(M):
        x0, y0 = PS[i]
        P2[x0].append(y0)

    total = 0
    for x0 in sorted(P2):
        for y0 in sorted(P2[x0]):
            s = bit_sum(y0 + 1)
            # debug(s, msg=":s")
            ret -= (total - s)
        for y0 in P2[x0]:
            bit_add(y0, 1)
            total += 1
    return ret


def naive(H, W, M, PS):
    ret = H * W - M
    for i in range(M):
        x0, y0 = PS[i]
        for j in range(i):
            x, y = PS[j]
            if x < x0 and y > y0:
                ret -= 1
                # debug(i, j, PS[i], PS[j], msg=":i,j,PS[i],PS[j]")

    return ret


def main():
    H, W, M = map(int, input().split())
    PS = []
    for _m in range(M):
        X, Y = map(int, input().split())
        PS.append((X, Y))
    PS.sort()
    print(solve(H, W, M, PS))


def random_test():
    from random import randint
    M = 3
    for i in range(1000):
        PS = []
        while len(PS) != M:
            p = (randint(1, 5), randint(1, 5))
            if p not in PS:
                PS.append(p)
        if solve(5, 5, M, PS) != naive(5, 5, M, PS):
            print(PS)
            break


# tests
T1 = """
4 3 2
2 2
3 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
10
"""

T2 = """
5 4 4
3 2
3 4
4 2
5 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
14
"""

T3 = """
5 5 2
2 2
2 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
23
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
