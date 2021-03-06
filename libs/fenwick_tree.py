"""
Fenwick Tree / Binary Indexed Tree (BIT)
"""


def init(n, value=0):
    global N, bit
    N = n
    bit = [0] * (N + 1)  # 1-origin
    if value != 0:
        for i in range(1, N + 1):
        bit_set(i, value)

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

# --- end of library ---


def main():
    # verified: https://atcoder.jp/contests/practice2/tasks/practice2_b
    N, Q = map(int, input().split())
    init(N)
    AS = list(map(int, input().split()))
    for i, a in enumerate(AS):
        bit_add(i + 1, a)

    for _q in range(Q):
        a, b, c = map(int, input().split())
        if a == 0:
            bit_add(b + 1, c)
        else:
            print(bit_sum(c) - bit_sum(b))


# tests
T1 = """
5 5
1 2 3 4 5
1 0 5
1 2 4
0 3 10
1 0 5
1 0 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
15
7
25
6
"""


def main_DP_Q():
    # verified: https://atcoder.jp/contests/dp/tasks/dp_q
    N = int(input())
    HS = list(map(int, input().split()))
    VS = list(map(int, input().split()))
    init(N + 1)  # 1-origin

    for i in range(N):
        h = HS[i]
        m = bit_max(h)
        bit_set(h, m + VS[i])

    print(bit_max(N))


# tests
T1_DP_Q = """
4
3 1 4 2
10 20 30 40
"""


def test_T1_DP_Q():
    """
    >>> as_input(T1_DP_Q)
    >>> main_DP_Q()
    60
    """


T2_DP_Q = """
1
1
10
"""


def test_T2_DP_Q():
    """
    >>> as_input(T2_DP_Q)
    >>> main_DP_Q()
    10
    """


T3_DP_Q = """
5
1 2 3 4 5
1000000000 1000000000 1000000000 1000000000 1000000000
"""


def test_T3_DP_Q():
    """
    >>> as_input(T3_DP_Q)
    >>> main_DP_Q()
    5000000000
    """


T4_DP_Q = """
9
4 2 5 8 3 6 1 7 9
6 8 8 4 6 3 5 7 5
"""


def test_T4_DP_Q():
    """
    >>> as_input(T4_DP_Q)
    >>> main_DP_Q()
    31
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
    # main()
    main_DP_Q()
